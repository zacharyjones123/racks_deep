# Tire Tools - Local Storage for Wheel Pros Tires
from datetime import time

import pyactiveresource
import pyprind

from data.WheelPros.Tags import Tags
from data.WheelPros.Tires.TireTools import TireTools
from excel_tools import ExcelTools
from shopify_tools import ShopifyTools
from urllib.error import HTTPError
import shopify

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
            # Built the tire name
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

#---------------------------------
#--Methods to run the program
#---------------------------------

def add_tires_shopify_tool():
    tires_info = ExcelTools.read_tire_data_usd(r'sheets/WheelPros/exp_12-05-2019_tireData.xlsx')
    ShopifyToolsTires.add_new_tires(tires_info)