#!/usr/bin/env python
"""
shopify_tools: All of the tools dealing with the Shopify
API
"""
import pyactiveresource
import shopify
from cred.cred import SHOP_URL
import pyprind
from urllib.error import HTTPError
import urllib.request
import time

from data.WheelPros.Tags import Tags
from data.WheelPros.Tires.TireTools import TireTools
from data.WheelPros.Wheels.WheelTools import WheelTools
from excel_tools import ExcelTools
from data.WheelPros.Kits.KitTools import KitTools

import mimetypes

# Wheel Tools - Local Storage for Wheel Pros Wheels
wheelTools = WheelTools()
# Tire Tools - Local Storage for Wheel Pros Tires
tireTools = TireTools()
# Kit Tools - Local Storage for Wheel Pros Kits
kitTools = KitTools()


def check_wheel_brand(param):
    brands = ["FUEL UTV",
              "MSA OFFROAD WHEELS",
              "XD ATV"]

    if param in brands:
        return True
    else:
        return False


class ShopifyTools:

    @staticmethod
    def is_url_image(url):
        mimetype, encoding = mimetypes.guess_type(url)
        return (mimetype and mimetype.startswith('image'))

    @staticmethod
    def check_url(url):
        """Returns True if the url returns a response code between 200-300,
           otherwise return False.
        """
        try:
            headers = {
                "Range": "bytes=0-10",
                "User-Agent": "MyTestAgent",
                "Accept": "*/*"
            }

            req = urllib.request.Request(url, headers=headers)
            response = urllib.request.urlopen(req)
            return response.code in range(200, 209)
        except Exception:
            return False

    @staticmethod
    def update_all_wheel_images():
        """
        This stems from a bug I found where the images exist
        but the program for some reason is not adding them in?
        # TODO: Add this to the list of bugs
        :return:
        """

    @staticmethod
    def is_image_and_ready(url):
        return ShopifyTools.is_url_image(url) and ShopifyTools.check_url(url)

    @staticmethod
    def start_shopify_api():
        """
        Method used to start the Shopify API and use methods
        :return: shop variable to call
        """
        # TODO: Need to add exceptions here in case it doesn't work
        shopify.ShopifyResource.set_site(SHOP_URL)
        return shopify.Shop.current
        return None

    @staticmethod
    def update_product_map_price(product, new_map_price):
        """
        This works right now but needs to be updated for multiple variants,

        The variants come in lists so that should be pretty easy to go through
        and change the one that needs to be changed.
        """
        update_product = shopify.Product.find(product.get_product_id())
        variant = shopify.Variant({'price': new_map_price, 'requires_shipping': True})
        if len(update_product.variants) == 1:
            update_product.variants = [variant]

        update_product.save()
        if update_product.errors:
            # something went wrong, see new_product.errors.full_messages() for example
            update_product.errors.full_messages()

    @staticmethod
    def get_all_product_ids(resource, **kwargs):
        """
        Method that will return all of the product resources

        :param resource: shopify.Product (I can probably expand this)
        :param kwargs: Other options to filter
        :return: a list of all resources
        """
        # TODO: Need to test this method
        while True:
            try:
                print("Getting All Product Ids:")
                resource_count = resource.count(**kwargs)
                resources = []
                if resource_count > 0:
                    bar = pyprind.ProgBar(len(range(1, ((resource_count - 1) // 250) + 2)), monitor=True)
                    for page in range(1, ((resource_count - 1) // 250) + 2):
                        # time.sleep(0.25)
                        kwargs.update({"limit": 250, "page": page})
                        resources.extend(resource.find(**kwargs))
                        bar.update()
                return resources
            except pyactiveresource.connection.Error:
                print("Internet is out, restarting server in 5 secodns")
                time.sleep(10)
            except TimeoutError:
                print("Timeout error has occured, restarting server in 5 seconds")
                time.sleep(10)
            except HTTPError:
                print("HTTP error has occured, restarting server in 5 seconds")
                time.sleep(10)

    @staticmethod
    def product_ids_to_products(resources):
        """
        Helper method to to get all the product ids from the resources
        :param resources: all resources from Shopify
        :return: Dictionary, key is product_id, value is resource
        """
        # TODO: Need to test this method
        product_dict = {}
        for r in resources:
            product_dict[r.id] = r
        return product_dict

    @staticmethod
    def add_new_wheel(wheel_variant):
        """
        Method that adds a new Wheel ProsWheel to Shopify
        :param wheel_variant: Wheel to add
        :return: Returns nothing
        """
        # TODO: Need to find a way to stream line this
        # TODO: Comment out the method

        if not check_wheel_brand(wheel_variant.get_whl_manufact_nm()):
            return

        # Make the tags that we want to add
        tags_to_add = []
        # Brand
        tags_to_add.append("Brand_" + wheel_variant.get_whl_manufact_nm())
        # Finish
        tags_to_add.append("Finish_" + wheel_variant.get_finish())
        # Bolt Pattern
        tags_to_add.append("Bolt Pattern_" + wheel_variant.get_bolt_pattern_metric())
        # Wheel Offset
        tags_to_add.append("Wheel Offset_" + wheel_variant.get_offset())
        # Wheel Size
        tags_to_add.append("Wheel Size_" + wheel_variant.get_size())

        # Need to find wheel price
        wheel_price1 = 0
        if wheel_variant.get_msrp_price() != 0:
            wheel_price1 = float(wheel_variant.get_msrp_price())
        elif wheel_variant.get_map_price() != 0:
            wheel_price1 = float(wheel_variant.get_map_price())
        else:
            wheel_price1 = 0

        # Make the bolt pattern setup
        lug_count = wheel_variant.get_lug_count()
        dist1 = str(int(float(wheel_variant.get_bolt_pattern_mm1())))
        bolt_pattern1 = lug_count + "x" + dist1
        # print(bolt_pattern1)
        dist2 = str(int(float(wheel_variant.get_bolt_pattern_mm2())))
        bolt_pattern2 = ""
        if int(dist2) != 0:
            bolt_pattern2 = lug_count + "x" + dist2

        # 2 cases
        # 1) Is a variant
        if wheelTools.has_variants(wheel_variant):
            product_id = wheelTools.find_product_id(wheel_variant)
            new_wheel_product = shopify.Product.find(product_id)
            variant = shopify.Variant({'price': wheel_price1,
                                       'option1': wheel_variant.get_size(),
                                       'option2': bolt_pattern1,
                                       'option3': wheel_variant.get_offset(),
                                       'quantity': 1,
                                       'sku': wheel_variant.get_upc(),
                                       'position': 1,
                                       'inventory_policy': "continue",
                                       'fulfillment_service': "manual",
                                       'inventory_management': "shopify",
                                       'inventory_quantity': 1,
                                       'taxable': False,
                                       'weight': float(wheel_variant.get_ship_weight()),
                                       'weight_unit': "g",  # g, kg
                                       'requires_shipping': True})

            # TODO: Need to organize this code
            # Below is all for when there is a second bolt pattern
            variant2 = shopify.Variant({'price': wheel_price1,
                                        'option1': wheel_variant.get_size(),
                                        'option2': bolt_pattern2,
                                        'option3': wheel_variant.get_offset(),
                                        'quantity': 1,
                                        'sku': wheel_variant.get_upc(),
                                        'position': 1,
                                        'inventory_policy': "continue",
                                        'fulfillment_service': "manual",
                                        'inventory_management': "shopify",
                                        'inventory_quantity': 1,
                                        'taxable': False,
                                        'weight': float(wheel_variant.get_ship_weight()),
                                        'weight_unit': "g",  # g, kg
                                        'requires_shipping': True})

            # print(type(new_wheel_product.variants))
            if bolt_pattern1 not in new_wheel_product.tags:
                new_wheel_product.tags += "," + bolt_pattern1
            if bolt_pattern2 not in new_wheel_product.tags:
                new_wheel_product.tags += "," + bolt_pattern2
            # print(new_wheel_product)
            new_wheel_product.variants.append(variant)
            if bolt_pattern2 != "":
                new_wheel_product.variants.append(variant2)
            # print("Variants: ", new_wheel_product.variants)

                # Get tags already put in
                tags = Tags()
                tags.string_to_tags(new_wheel_product.tags)
                # Now, we can go through and add the tags we want
                for t in tags_to_add:
                    if not tags.is_a_tag(t) and "nan" not in t:
                        tags.add_tag(t)
            new_wheel_product.save()
            wheelTools.add_wheel(product_id, wheel_variant)

            # TODO: Need to organize this code
            # Below is all for when there is a second bolt pattern

        # 2) Is not a variant
        else:
            # Update a product
            new_wheel_product = shopify.Product()
            new_wheel_product.options = [{'name': 'Tire Size'}, {'name': 'Bolt Pattern'}, {'name': 'Offset'}]
            new_wheel_product.title = wheel_variant.get_style_description()
            new_wheel_product.vendor = "Wheel Pros"
            new_wheel_product.product_type = "Wheels"
            new_wheel_product.body_html = """<b>%s</b>
                                    <p>%s</p>
                                    """ % (wheel_variant.get_style_description(),
                                           wheel_variant.get_part_num_description())
            variant = shopify.Variant({'price': wheel_price1,
                                       'option1': wheel_variant.get_size(),
                                       'option2': bolt_pattern1,
                                       'option3': wheel_variant.get_offset(),
                                       'quantity': 1,
                                       'sku': wheel_variant.get_upc(),
                                       'position': 1,
                                       'inventory_policy': "continue",
                                       'fulfillment_service': "manual",
                                       'inventory_management': "shopify",
                                       'inventory_quantity': 1,
                                       'taxable': False,
                                       'weight': float(wheel_variant.get_ship_weight()),
                                       'weight_unit': "g",  # g, kg
                                       'requires_shipping': True})
            # TODO: Need to organize this code
            # Below is all for when there is a second bolt pattern
            variant2 = shopify.Variant({'price': wheel_price1,
                                       'option1': wheel_variant.get_size(),
                                        'option2': bolt_pattern2,
                                        'option3': wheel_variant.get_offset(),
                                       'quantity': 1,
                                       'sku': wheel_variant.get_upc(),
                                       'position': 1,
                                       'inventory_policy': "continue",
                                       'fulfillment_service': "manual",
                                       'inventory_management': "shopify",
                                       'inventory_quantity': 1,
                                       'taxable': False,
                                       'weight': float(wheel_variant.get_ship_weight()),
                                       'weight_unit': "g",  # g, kg
                                       'requires_shipping': True})

            new_wheel_product.variants = [variant]
            if bolt_pattern2 != "":
                new_wheel_product.variants.append(variant2)

            new_wheel_product.tags = """WheelPros,
                        Wheels,
                        %s, 
                        %s,
                        %s,
                        %s,
                        %s,
                        %s,
                        %s""" % (wheel_variant.get_part_number(),
                                 wheel_variant.get_size(),
                                 wheel_variant.get_finish(),
                                 wheel_variant.get_offset(),
                                 wheel_variant.get_upc(),
                                 bolt_pattern1,
                                 bolt_pattern2)

            # Get tags already put in
            tags = Tags()
            tags.string_to_tags(new_wheel_product.tags)
            # Now, we can go through and add the tags we want
            for t in tags_to_add:
                if not tags.is_a_tag(t) and "nan" not in t:
                    tags.add_tag(t)

            image = shopify.Image()
            file_name = "%s" % (wheel_variant.get_wheel_image())
            if ShopifyTools.is_image_and_ready(file_name):
                image.src = file_name
            else:
                print(wheel_variant.get_upc)
                print(wheel_variant.get_style_description())
                print("-----------------")

            new_wheel_product.images = [image]
            new_wheel_product.save()

            wheelTools.add_wheel(new_wheel_product.id, wheel_variant)

            # print("PRODUCT ID: ", new_wheel_product.id)
            new_wheel_product.save()  # returns false if the record is invalid
            if new_wheel_product.errors:
                # something went wrong, see new_product.errors.full_messages() for example
                print(new_wheel_product.errors.full_messages())

    @staticmethod
    def add_new_wheels(wheels):
        """
        Method used to add Wheel Pros Wheels
        :param wheels: wheels added
        :return: Nothing
        """
        # TODO: Need to test this method

        bar = pyprind.ProgBar(len(wheels), monitor=True, update_interval=.1)
        total_added = 1
        for i in range(len(wheels)):
            try:
                w = wheels[i]
                # print("adding: ", w.get_style_description())
                ShopifyTools.add_new_wheel(w)
                bar.update(item_id=str(total_added))
                total_added += 1
            # This worked!!! I don't know what happened, but it worked!
            # The error was caught, and then it continued. It happened
            # at 5221

            except pyactiveresource.connection.Error:
                print("Internet is out, restarting server in 5 secodns")
                i -= 1
                time.sleep(10)
            except TimeoutError:
                total_added -= 1
                i -= 1
                print("Timeout error has occured, restarting server in 5 seconds")
                time.sleep(10)
            except HTTPError:
                total_added -= 1
                i -= 1
                print("HTTP error has occured, restarting server in 5 seconds")
                time.sleep(10)

            print(bar)

    @staticmethod
    def update_wheel(wheel_variant):
        """
        Method used to update wheel with another wheel
        :param wheel_variant: wheel to update with
        :return: report of what happened
        """
        pass

    @staticmethod
    def update_wheels(wheels):
        """
        Uses helper method update_wheel to update
        all of the wheels in the wheels array
        :param wheels: array of wheels to udpate
        :return: report of what happened
        """
        pass

    @staticmethod
    def update_wheels_in_chunks(wheels, total_wheels):
        """
        Way of updating wheels in chunks
        :param wheels: wheels ot be added
        :param total_wheels: total number of wheels to add
        :return: report of what happened
        """
        pass

    @staticmethod
    def add_new_wheels_in_chunks(wheels, total_wheels):
        """
        Method used to add Wheel Pros Wheels
        :param wheels: wheels added
        :param total_wheels: total wheels to be added
        :return: Nothing
        """
        # TODO: Need to test this method

        bar = pyprind.ProgBar(total_wheels, monitor=True, update_interval=.1)
        total_added = 1
        # This is for each of the sections
        sections_done = 1
        for i in range(len(wheels)):
            total_in_section_done = 1
            for j in range(len(wheels[i])):
                try:
                    if i * j >= -1:
                        time.sleep(0.25)
                        w = wheels[i][j]
                        ShopifyTools.add_new_wheel(w)
                        bar_graph_string = "Section: " + str(sections_done)
                        bar_graph_string += " - Index: " + str(total_added)
                        bar.update(item_id=bar_graph_string)
                        total_added += 1
                        total_in_section_done += 1
                        # This worked!!! I don't know what happened, but it worked!
                        # The error was caught, and then it continued. It happened
                        # at 5221

                except pyactiveresource.connection.Error:
                    print("Internet is out, restarting server in 5 seconds")
                    j -= 1
                    time.sleep(10)
                except TimeoutError:
                    total_added -= 1
                    j -= 1
                    print("Timeout error has occured, restarting server in 5 seconds")
                    time.sleep(10)
                except HTTPError:
                    total_added -= 1
                    j -= 1
                    print("HTTP error has occured, restarting server in 5 seconds")
                    time.sleep(10)
            sections_done += 1

        print(bar)

    @staticmethod
    def add_new_tire(tire_variant):
        """
        Method that adds a new Wheel Pros Tire to Shopify
        :param tire_variant: Tire to add:
        :return: Returns nothing
        """
        # TODO: Need to find a way to stream line this
        # TODO: Comment out the method

        # Make the tags that we want to add
        tags_to_add = []
        # Ply
        if tire_variant.get_ply() != "0":
            tags_to_add.append("Ply_"+tire_variant.get_ply())
        # Speed Rating
        #tags_to_add.append("Speed Rating_"+tire_variant.get_speed_rating())
        # Rim Diameter
        tags_to_add.append("Rim Diameter_"+tire_variant.get_rim_diameter()+"\"")
        # Tire Diameter
        #tags_to_add.append("Tire Diameter_"+tire_variant.get_tire_diameter())
        # Full Model Name
       # tags_to_add.append("Model_"+tire_variant.get_full_model_name())
        # Construction Type
        tags_to_add.append("Construction Type_"+tire_variant.get_construction_type())
        # Terrain
        tags_to_add.append("Terrain_"+tire_variant.get_terrain())

        # Need to find out the correct price
        if float(tire_variant.get_map()) == 0:
            price_for_tire = tire_variant.get_mrsp()
        else:
            price_for_tire = tire_variant.get_map()

        # 2 cases
        # 1) Is a variant
        if tireTools.has_variants(tire_variant):
            product_id = tireTools.find_product_id(tire_variant)
            new_tire_product = shopify.Product.find(product_id)
            variant = shopify.Variant({'price': float(price_for_tire),
                                       'option1': tire_variant.get_tire_size(),
                                       'quantity': 1,
                                       'sku': tire_variant.get_upc(),
                                       'position': 1,
                                       'inventory_policy': 'continue',
                                       'fulfillment_service': 'manual',
                                       'inventory_management': 'shopify',
                                       'inventory_quantity': 1,
                                       'taxable': False,
                                       'weight': float(tire_variant.get_weight()),
                                       'weight_unit': 'g',
                                       'requires_shipping': True})
            # Get tags already put in
            tags = Tags()
            tags.string_to_tags(new_tire_product.tags)
            # Now, we can go through and add the tags we want
            for t in tags_to_add:
                if not tags.is_a_tag(t) and "nan" not in t:
                    tags.add_tag(t)

            new_tire_product.tags = tags.tags_to_string()
            new_tire_product.variants.append(variant)
            new_tire_product.save()
            tireTools.add_tire(product_id, tire_variant)
            # 2) Is not a variant
        else:
            new_tire_product = shopify.Product()
            new_tire_product.options = [{'name': 'Tire Size'}]
            #Built the tire name
            new_tire_product.title = tire_variant.get_full_model_name()
            new_tire_product.vendor = 'Wheel Pros'
            new_tire_product.product_type = 'Tires'
            new_tire_product.body_html = """<b>%s</b>
                                   <p>%s</p>
                                   """ % (tire_variant.get_tire_description(), tire_variant.get_part_num())
            variant = shopify.Variant({'price': float(price_for_tire),
                                       'option1': tire_variant.get_tire_size(),
                                       'quantity': 1,
                                       'sku': tire_variant.get_upc(),
                                       'position': 1,
                                       'inventory_policy': 'continue',
                                       'fulfillment_service': 'manual',
                                       'inventory_management': 'shopify',
                                       'inventory_quantity': 1,
                                       'taxable': False,
                                       'weight': float(tire_variant.get_weight()),
                                       'weight_unit': 'g',
                                       'requires_shipping': True})
            new_tire_product.variants = [variant]

            new_tire_product.tags = """WheelPros,
                       Tires,
                       %s,
                       %s,
                       %s,
                       %s,""" % (ShopifyTools.find_tire_brand(tire_variant.get_tire_description()),
                                 tire_variant.get_part_num(),
                                 tire_variant.get_tire_size(),
                                 tire_variant.get_upc())

            # Get tags already put in
            tags = Tags()
            tags.string_to_tags(new_tire_product.tags)
            # Now, we can go through and add the tags we want
            for t in tags_to_add:
                if not tags.is_a_tag(t) and "nan" not in t:
                    tags.add_tag(t)

            image = shopify.Image()
            file_name = "https://images.wheelpros.com/h%s.png" % (tire_variant.get_picture_cd())
            image.src = file_name
            new_tire_product.images = [image]
            new_tire_product.save()

            tireTools.add_tire(new_tire_product.id, tire_variant)
            new_tire_product.save()  # returns false if the record is invalid
            if new_tire_product.errors:
                # something went wrong, see new_product.errors.full_messages() for example
                new_tire_product.errors.full_messages()

    @staticmethod
    def add_new_tires(tires):
        """
        Method used to add Wheel Pros Tires
        :param tires: Tires to be added
        :return: Nothing
        """
        # TODO: Need to test this method

        bar = pyprind.ProgBar(len(tires), monitor=True, update_interval=.1)
        total_added = 1
        for t in range(len(tires)):
            try:
                ShopifyTools.add_new_tire(tires[t])
                bar.update(item_id=str(total_added))
                total_added += 1
            except pyactiveresource.connection.Error:
                print("Internet is out, restarting server in 5 secodns")
                total_added -= 1
                t -= 1
                time.sleep(10)
            except TimeoutError:
                total_added -= 1
                t -= 1
                print("Timeout error has occured, restarting server in 5 seconds")
                time.sleep(10)
            except HTTPError:
                total_added -= 1
                t -= 1
                print("HTTP error has occured, restarting server in 5 seconds")
                time.sleep(10)

    @staticmethod
    def find_tire_brand(tire_description):
        """
        Method used as a smart way to add tags
        :param tire_description: The title of the tire to be shown
        :return: Returns the brand
        """
        # TODO: Need to test this method
        tire_dict = {'MOTOCLAW': 'MOTOCLAW',
                     'MOTOBOSS': 'MOTOBOSS',
                     'MOTOFORCE': 'MOTOFORCE',
                     'MOTOHAMMER': 'MOTOHAMMER',
                     'EFX MOTOHAVOK': 'EFX MOTOHAVOK',
                     'MOTOMAX': 'MOTOMAX',
                     'MOTOVATOR': 'MOTOVATOR',
                     'MOTOVATOR R/T': 'MOTOVATOR R/T',
                     'SLINGER': 'SLINGER',
                     'MOTOMTC': 'MOTOMTC'}
        for t in tire_dict:
            if t in tire_description:
                return tire_dict[t]
        return "No Brand"

    @staticmethod
    def get_all_wheel_pros_wheel_products_product_ids():
        """
        Method to return all wheel product ids
        :return: wheel product ids
        """
        # TODO: Need a way to make sure this is working correctly. Not sure how to set up test suite

        # Method that will get all Shopify.Product from shopify
        product_dict = ShopifyTools.product_ids_to_products(ShopifyTools.get_all_product_ids(shopify.Product))
        # List to return
        wheel_products = []
        # Go through all Shopify.Product from shopify
        for p in product_dict:
            # Check if the information is correct for Wheel Pros, Wheels
            if product_dict[p].vendor == "Wheel Pros" and product_dict[p].product_type == "Wheels":
                # Add the product id to the list
                wheel_products.append(p)
        # Return the wheel product ids
        return wheel_products

    @staticmethod
    def get_all_wheel_variants_skus_from_shopify():
        """
        Method to return all wheel variants skus from shopify
        :return: wheel variants skus from shopify
        """
        # TODO: Need a way to make sure this is working correctly. Not sure how to set up test suite

        # Method that will get all Shopify.Product from shopify
        product_dict = ShopifyTools.product_ids_to_products(ShopifyTools.get_all_product_ids(shopify.Product))
        # List to return
        wheel_variants_skus = []
        # Go through all Shopify.Product from shopify
        for p in product_dict:
            # Check if the information is correct for Wheel Pros, Wheels
            if product_dict[p].vendor == "Wheel Pros" and product_dict[p].product_type == "Wheels":
                # go through the variants
                for v in product_dict[p].variants:
                    # Add the sku (or upc) for all the variants
                    wheel_variants_skus.append(v.sku)
        # Return all of the wheel variant's skus from shopify
        return wheel_variants_skus

    @staticmethod
    def get_all_wheel_variants_in_shopify():
        """
        Method is used to get all of the wheel variants in shopify, so then it can
        be compared to the local versions.
        :return: Returns all wheel variants (List of WheelVariants)
        """

        # TODO: Need a way to make sure this is working correctly. Not sure how to set up test suite

        # Helper method to get the skus so the products can be found
        wheel_variants_skus = ShopifyTools.get_all_wheel_variants_skus_from_shopify()
        # List to be returned
        wheel_variants_in_shopify = []
        # Loop through the wheel variants in currently in local
        for wv in wheelTools.get_wheel_variants_list():
            # Check if the upc local is the same as the shopify version
            if wv.get_upc() in wheel_variants_skus:
                # Add it into the list
                wheel_variants_in_shopify.append(wv)
        # Return the wheel variants in shopify
        return wheel_variants_in_shopify

    @staticmethod
    def get_new_kit(kit_variant):
        # TODO: Make add_new_kit() method
        pass

    @staticmethod
    def add_new_kits(kits):
        # TODO: Make add_new_kits() method
        # TODO: Need to test this method

        bar = pyprind.ProgBar(len(kits), monitor=True, update_interval=.1)
        total_added = 1
        for i in range(len(kits)):
            try:
                w = kits[i]
                ShopifyTools.add_new_kit(w)
                bar.update(item_id=str(total_added))
                total_added += 1
            # This worked!!! I don't know what happened, but it worked!
            # The error was caught, and then it continued. It happened
            # at 5221

            except pyactiveresource.connection.Error:
                print("Internet is out, restarting server in 5 secodns")
                i -= 1
                time.sleep(10)
            except TimeoutError:
                total_added -= 1
                i -= 1
                print("Timeout error has occured, restarting server in 5 seconds")
                time.sleep(10)
            except HTTPError:
                total_added -= 1
                i -= 1
                print("HTTP error has occured, restarting server in 5 seconds")
                time.sleep(10)

        print(bar)

    @staticmethod
    def delete_all_wheels():
        """
        This method is used to delete all Wheel Pros - Wheels
        :return: This method does not return anything
        """
        print("Deleting All Wheel Pro Wheels")
        # Helper method to get all of the product ids needed
        # wheel_products = ShopifyTools.get_all_wheel_pros_wheel_products_product_ids()
        # Bar Graph start
        # print(wheelTools.get_wheels())
        wheels_copy = wheelTools.get_wheels().copy()
        bar = pyprind.ProgBar(len(wheels_copy), monitor=True, update_interval=.1)
        # Keeps track of total deleted
        total_deleted = 0
        # Go through all wheel product ids found
        print(wheels_copy)
        for p in wheels_copy:
            # Try to delete, ,know that it might not exist
            # TODO: May need to add in more exceptions
            try:
                # Shopify API - to get the product using the Product ID
                deletes_product = shopify.Product.find(p)
                # Delete the product
                deletes_product.destroy()
                # Delete the product from the local database
                wheelTools.delete_wheel(p)
                # Add 1 knowing that the delete worked
                total_deleted += 1
            except KeyError:
                # Exception if it doesn't exist
                print(p, " was not found!")
            bar.update(item_id=str(total_deleted))
        # Print out the statistics of the method
        print(bar)
        # TODO: Add a way to check if the method successfully deleted

    @staticmethod
    def build_wheels():
        """
        Method I built in order to build the wheels list
        from the wheel variants from Shopify
        :return: Nothing, but updates wheels in WheelTools
        """
        # TODO: Need to simplify this method, it has 3 for loops

        # Method that will get all Shopify.Product from shopify
        product_dict = ShopifyTools.product_ids_to_products(ShopifyTools.get_all_product_ids(shopify.Product))

        # Build the wheels in WheelTools
        # Go through all products on shopify
        for p in product_dict:
            # Go through there variants
            for v in product_dict[p].variants:
                # Go through wheel_variants locally
                for w in wheelTools.get_wheel_variants_list():
                    # If this is the correct wheel variant
                    if v.sku == w.get_upc():
                        # Add it to wheels
                        wheelTools.add_wheel(p, w)

    @staticmethod
    def chunks(l, n):
        """
        Method made to split long product lists into even sized chunks
        This comes from a bug with importing a large amount of products
        at once
        :param l: list you are cutting
        :param n: number in each section
        :return:
        """
        """Yield successive n-sized chunks from l."""
        for i in range(0, len(l), n):
            yield l[i:i + n]

    @staticmethod
    def add_new_kit(kit_variant):
        # 2 cases
        # 1) Is a variant
        if kitTools.has_variants(kit_variant):
            product_id = kitTools.find_product_id(kit_variant)
            new_kit_product = shopify.Product.find(product_id)
            variant = shopify.Variant({'price': kit_variant.get_price(),
                                       'option1': kit_variant.get_wheel(),
                                       'option2': kit_variant.get_tire(),
                                       'sku': "a",
                                       'position': 1,
                                       'inventory_policy': "continue",
                                       'fulfillment_service': "manual",
                                       'inventory_management': "shopify",
                                       'inventory_quantity': 1,
                                       'taxable': False,
                                       'weight': 0,
                                       'weight_unit': "g",  # g, kg
                                       'requires_shipping': True})

            new_kit_product.tags += ","+kit_variant.get_tire()

            new_kit_product.variants.append(variant)
            new_kit_product.save()
            kitTools.add_kit(product_id, kit_variant)

            # TODO: Need to organize this code
            # Below is all for when there is a second bolt pattern

        # 2) Is not a variant
        else:
            # Update a product
            new_kit_product = shopify.Product()
            new_kit_product.options = [{'name': 'Wheel'}, {'name': 'Tire'}]
            new_kit_product.title = kit_variant.get_kit_name()
            new_kit_product.vendor = "Racks Deep Custom Performance"
            new_kit_product.product_type = "Kits"
            new_kit_product.body_html = """<b>%s</b>
                                            """ % (kit_variant.get_kit_name())
            variant = shopify.Variant({'price': kit_variant.get_price(),
                                       'option1': kit_variant.get_wheel(),
                                       'option2': kit_variant.get_tire(),
                                       'sku': "a",
                                       'position': 1,
                                       'inventory_policy': "continue",
                                       'fulfillment_service': "manual",
                                       'inventory_management': "shopify",
                                       'inventory_quantity': 1,
                                       'taxable': False,
                                       'weight': 0,
                                       'weight_unit': "g",  # g, kg
                                       'requires_shipping': True})
            new_kit_product.variants = [variant]
            new_kit_product.tags = """WheelPros,
                                      Kits,
                                      %s,
                                      %s
                                   """ % (kit_variant.get_wheel(),
                                         kit_variant.get_tire())

            #image = shopify.Image()
            #file_name = "%s" % (wheel_variant.get_wheel_image())
            #if ShopifyTools.is_image_and_ready(file_name):
            #    image.src = file_name
           # else:
            #    print(wheel_variant.get_upc)
            #    print(wheel_variant.get_style_description())
            #    print("-----------------")

           # new_wheel_product.images = [image]
            new_kit_product.save()

            kitTools.add_kit(new_kit_product.id, kit_variant)
            if new_kit_product.errors:
                # something went wrong, see new_product.errors.full_messages() for example
                print(new_kit_product.errors.full_messages())


shop = ShopifyTools.start_shopify_api()
wheelTools.load_wheel_variants_from_file()
spread_sheet_name = "sheets/WheelPros/bug_fix_producttechdatausd.xlsx"
wheelTools.set_wheel_variants_list(ExcelTools.read_product_technical_data_usd(spread_sheet_name))

# This is all of the products, so we can
product_dict = ShopifyTools.product_ids_to_products(ShopifyTools.get_all_product_ids(shopify.Product))
# Turn this into Wheels, and add them to WheelTools

# This is used to build the wheels for WheelTools
ShopifyTools.build_wheels()


def add_wheels_shopify_tool():
    wheels_info = ExcelTools.read_product_technical_data_usd(r'sheets/WheelPros/exp_11-28-2019_producttechdatausd.xlsx')
    # Need to split this up into 100 chunks
    wheel_info_chunks = list(ShopifyTools.chunks(wheels_info, 100))
    ShopifyTools.add_new_wheels_in_chunks(wheel_info_chunks, len(wheels_info))
    wheelTools.set_wheel_variants_list(wheels_info)
    #wheelTools.save_wheel_variants_to_file()


def add_tires_shopify_tool():
    tires_info = ExcelTools.read_tire_data_usd(r'sheets/WheelPros/exp_12-05-2019_tireData.xlsx')
    ShopifyTools.add_new_tires(tires_info)


def delete_wheels_shopify_tool():
    ShopifyTools.delete_all_wheels()
    #wheelTools.save_wheel_variants_to_file()


def add_kits_shopify_tool():
    kits_info = ExcelTools.read_kit_data(r'sheets/WheelPros/wheel_pros_kits.xlsx')
    ShopifyTools.add_new_kits(kits_info)


# delete_wheels_shopify_tool()
add_wheels_shopify_tool()
