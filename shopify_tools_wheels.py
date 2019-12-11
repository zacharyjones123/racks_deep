# Wheel Tools - Local Storage for Wheel Pros Wheels
from datetime import time

import pyactiveresource
import pyprind

from data.WheelPros.Tags import Tags
from data.WheelPros.Wheels.WheelTools import WheelTools
from excel_tools import ExcelTools
from shopify_tools import ShopifyTools
from urllib.error import HTTPError
import shopify

wheelTools = WheelTools()

class ShopifyToolsWheels:
    @staticmethod
    def update_all_wheel_images():
        """
        This stems from a bug I found where the images exist
        but the program for some reason is not adding them in?
        # TODO: Add this to the list of bugs
        :return:
        """

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
    def add_new_wheel(wheel_variant):
        """
        Method that adds a new Wheel ProsWheel to Shopify
        :param wheel_variant: Wheel to add
        :return: Returns nothing
        """
        # TODO: Need to find a way to stream line this
        # TODO: Comment out the method

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
        dist1 = str(int(float(wheel_variant.get_bolt_pattern_mm_1())))
        bolt_pattern1 = lug_count + "x" + dist1
        # print(bolt_pattern1)
        dist2 = str(int(float(wheel_variant.get_bolt_pattern_mm_2())))
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
                                       'weight': float(wheel_variant.get_shipping_weight()),
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
                                        'weight': float(wheel_variant.get_shipping_weight()),
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

            new_wheel_product.tags = tags.tags_to_string()
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
                                       'weight': float(wheel_variant.get_shipping_weight()),
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
                                       'weight': float(wheel_variant.get_shipping_weight()),
                                       'weight_unit': "g",  # g, kg
                                       'requires_shipping': True})

            new_wheel_product.variants = [variant]
            if bolt_pattern2 != "":
                new_wheel_product.variants.append(variant2)

            new_wheel_product.tags = """WheelPros,
                        Wheels"""

            # Get tags already put in
            tags = Tags()
            tags.string_to_tags(new_wheel_product.tags)
            # Now, we can go through and add the tags we want
            for t in tags_to_add:
                if not tags.is_a_tag(t) and "nan" not in t:
                    tags.add_tag(t)

            new_wheel_product.tags = tags.tags_to_string()

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
                ShopifyToolsWheels.add_new_wheel(w)
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
                        ShopifyToolsWheels.add_new_wheel(w)
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
        wheel_variants_skus = ShopifyToolsWheels.get_all_wheel_variants_skus_from_shopify()
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

#---------------------------------
#--Methods to run the program
#---------------------------------
def add_wheels_shopify_tool():
    wheels_info = ExcelTools.read_product_technical_data_usd(r'sheets/WheelPros/exp_11-28-2019_producttechdatausd.xlsx')
    # Need to split this up into 100 chunks
    wheel_info_chunks = list(ShopifyTools.chunks(wheels_info, 100))
    ShopifyToolsWheels.add_new_wheels_in_chunks(wheel_info_chunks, len(wheels_info))
    wheelTools.set_wheel_variants_list(wheels_info)
    #wheelTools.save_wheel_variants_to_file()

def delete_wheels_shopify_tool():
    ShopifyToolsWheels.delete_all_wheels()
    #wheelTools.save_wheel_variants_to_file()