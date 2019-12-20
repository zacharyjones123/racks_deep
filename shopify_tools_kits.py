from datetime import time

import pyactiveresource
import pyprind

from data.WheelPros.Tags import Tags
from data.WheelPros.Kits.KitTools import KitTools
from excel_tools import ExcelTools
from shopify_tools import ShopifyTools
from urllib.error import HTTPError
import shopify

# Kit Tools - Local Storage for Wheel Pros Kits
kitTools = KitTools()


class ShopifyToolsKits:
    @staticmethod
    def add_new_kits(kits):
        # TODO: Make add_new_kits() method
        # TODO: Need to test this method

        bar = pyprind.ProgBar(len(kits), monitor=True, update_interval=.1)
        total_added = 1
        for i in range(len(kits)):
            try:
                w = kits[i]
                ShopifyToolsKits.add_new_kit(w)
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
    def add_new_kit(kit_variant):
        # 2 cases
        # 1) Is a variant

        # Tags
        tags_to_add = []

        # Size
        tags_to_add.append("Size_"+kit_variant.get_size())
        tags_to_add.append(kit_variant.get_tire())
        tags_to_add.append(kit_variant.get_wheel())

        if kitTools.has_variants(kit_variant):
            product_id = kitTools.find_product_id(kit_variant)
            new_kit_product = shopify.Product.find(product_id)
            variant = shopify.Variant({'price': kit_variant.get_msrp(),
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

            # Get tags already put in
            tags = Tags()
            tags.string_to_tags(new_kit_product.tags)
            # Now, we can go through and add the tags we want
            for t in tags_to_add:
                if not tags.is_a_tag(t) and "nan" not in t:
                    tags.add_tag(t)

            new_kit_product.tags = tags.tags_to_string()

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
                                            <h1>All Kits come mounted with new lugnuts</h1>
                                            """ % (kit_variant.get_kit_name())
            variant = shopify.Variant({'price': kit_variant.get_msrp(),
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
                                      Kits
                                      """

            # Get tags already put in
            tags = Tags()
            tags.string_to_tags(new_kit_product.tags)
            # Now, we can go through and add the tags we want
            for t in tags_to_add:
                if not tags.is_a_tag(t) and "nan" not in t:
                    tags.add_tag(t)

            new_kit_product.tags = tags.tags_to_string()

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

    @staticmethod
    def update_kit(kit_variant):
        pass

    @staticmethod
    def update_kits(kits):
        pass

    @staticmethod
    def delete_kit(kit_variant):
        pass

    @staticmethod
    def delete_kits(kits):
        pass
#---------------------------------
#--Methods to run the program
#---------------------------------

def add_kits_shopify_tool():
    kits_info = ExcelTools.read_kit_data(r'sheets/WheelPros/wheel_pros_kits.xlsx')
    ShopifyToolsKits.add_new_kits(kits_info)

def update_kits_shopify_tool():
    pass

def delete_kits_shopify_tool():
    pass