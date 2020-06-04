from datetime import time

import pyactiveresource
import pyactiveresource.connection
import pyprind

import time

from data.WheelPros.Tags import Tags
from data.WheelPros.Tires.TireTools import TireTools
from data.WheelPros.Tires.TireVariants import TireVariants
from utils.excel_tools import ExcelTools
from shopify_tools import ShopifyTools
from urllib.error import HTTPError
import shopify

# Tire Tools - Local Storage for Wheel Pros Tires
tireTools = TireTools()


class ShopifyToolsTires:
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
            tags_to_add.append("Ply_" + tire_variant.get_ply())
        # Speed Rating
        # tags_to_add.append("Speed Rating_"+tire_variant.get_speed_rating())
        # Rim Diameter
        tags_to_add.append("Rim Diameter_" + tire_variant.get_rim_diameter() + "\"")
        # Tire Diameter
        # tags_to_add.append("Tire Diameter_"+tire_variant.get_tire_diameter())
        # Full Model Name
        # tags_to_add.append("Model_"+tire_variant.get_full_model_name())
        # Construction Type
        tags_to_add.append("Construction Type_" + tire_variant.get_construction_type())
        # Terrain
        tags_to_add.append("Terrain_" + tire_variant.get_terrain())

        # Need to find out the correct price
        if float(tire_variant.get_map_price()) == 0:
            price_for_tire = tire_variant.get_mrsp_price()
        else:
            price_for_tire = tire_variant.get_map_price()

        # 2 cases
        # 1) Is a variant
        if tireTools.has_variants(tire_variant):
            product_id = tireTools.find_product_id(tire_variant)
            new_tire_product = shopify.Product.find(product_id)
            variant = shopify.Variant({'price': float(price_for_tire),
                                       'option1': tire_variant.get_tire_size_description(),
                                       'quantity': 1,
                                       'sku': tire_variant.get_upc(),
                                       'position': 1,
                                       'inventory_policy': 'deny',
                                       'fulfillment_service': 'manual',
                                       'inventory_management': 'shopify',
                                       'inventory_quantity': tire_variant.get_curr_stock(),
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
            # Built the tire name
            new_tire_product.title = tire_variant.get_full_model_name()
            new_tire_product.vendor = 'Wheel Pros'
            new_tire_product.product_type = 'Tires'
            new_tire_product.body_html = """<b>%s</b>
                                   <p>%s</p>
                                   """ % (tire_variant.get_tire_description(), tire_variant.get_part_num())
            variant = shopify.Variant({'price': float(price_for_tire),
                                       'option1': tire_variant.get_tire_size_description(),
                                       'quantity': 1,
                                       'sku': tire_variant.get_upc(),
                                       'position': 1,
                                       'inventory_policy': 'deny',
                                       'fulfillment_service': 'manual',
                                       'inventory_management': 'shopify',
                                       'inventory_quantity': tire_variant.get_curr_stock(),
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
                       %s,""" % (tire_variant.get_full_model_name(),
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
            file_name = tire_variant.get_picture_cd()
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
                ShopifyToolsTires.add_new_tire(tires[t])
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
    def update_new_tire(tire_variant):
        #Need to get a dictionary of all variants
        all_tire_variants = ShopifyToolsTires.get_all_tire_variants_in_shopify()
        print(all_tire_variants)

        #Now, need to get the right one
        update_tire = shopify.Product.find(all_tire_variants[tire_variant.get_upc()])

        #Now, find the variant that we want to change
        for v in range(len(update_tire.variants)):
            if update_tire.variants[v].sku == tire_variant.get_upc():
                print("The price was changed")
                update_tire.variants[v].price = 777

        update_tire.save()
        if update_tire.errors:
            #something went, wrong, see new_product.errors.full_messages() for example
            update_tire.errors.full_messages()

    @staticmethod
    def update_new_tires(tires):
        pass

    @staticmethod
    def delete_tire(tire_variant):
        pass

    @staticmethod
    def delete_tires(tires):
        pass

    @staticmethod
    def get_all_tire_variants_skus_from_shopify():
        """
        Method to return all wheel variants skus from shopify
        :return: wheel variants skus from shopify
        """
        # TODO: Need a way to make sure this is working correctly. Not sure how to set up test suite

        # Method that will get all Shopify.Product from shopify
        product_dict = ShopifyTools.product_ids_to_products(ShopifyTools.get_all_product_ids(shopify.Product))
        # List to return
        tire_variants_skus = {}
        # Go through all Shopify.Product from shopify
        for p in product_dict:
            # Check if the information is correct for Wheel Pros, Wheels
            if product_dict[p].vendor == "Wheel Pros" and product_dict[p].product_type == "Tires":
                # go through the variants
                for v in product_dict[p].variants:
                    # Add the sku (or upc) for all the variants
                    tire_variants_skus[v.sku] = p
        # Return all of the wheel variant's skus from shopify
        return tire_variants_skus

    @staticmethod
    def get_all_tire_variants_in_shopify():
        """
        Method is used to get all of the wheel variants in shopify, so then it can
        be compared to the local versions.
        :return: Returns all wheel variants (List of WheelVariants)
        """

        # TODO: Need a way to make sure this is working correctly. Not sure how to set up test suite

        # Helper method to get the skus so the products can be found
        tire_variants_skus = ShopifyToolsTires.get_all_tire_variants_skus_from_shopify()
        # List to be returned
        # Loop through the wheel variants in currently in local

        all_products = list(set(tire_variants_skus.values()))

        for w in all_products:
            temp_product = shopify.Product.find(w)
            # Now, need to see if this is a Wheel
            #print(w," - ", wheel_variants_skus[w])
        return tire_variants_skus

#---------------------------------
#--Methods to run the program
#---------------------------------

def add_tires_shopify_tool(spread_sheet_name):
    tires_info = ExcelTools.read_tire_data_usd(spread_sheet_name)
    ShopifyToolsTires.add_new_tires(tires_info)

def update_tires_shopify_tool():
    tire_variant = TireVariants(None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None,
                                None)
    tire_variant.set_mrsp_price("777")
    tire_variant.set_upc("806454490004.0")
    ShopifyToolsTires.update_new_tire(tire_variant)

def delete_tires_shopify_tool():
    pass

#update_tires_shopify_tool()
add_tires_shopify_tool(r'sheets/WheelPros/tires_exp_5-28-2020.xlsx')