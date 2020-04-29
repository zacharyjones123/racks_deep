import time

import pyactiveresource
import pyprind
import os

from data.DS18.Products.DS18ProductsTools import DS18ProductsTools
from data.WheelPros.Tags import Tags
from utils.excel_tools import ExcelTools
from urllib.error import HTTPError
import shopify

# DS18Tools - Local Storage for DS18 Products
ds18Tools = DS18ProductsTools()


class ShopifyToolsDS18:
    @staticmethod
    def get_picture(model_name):
        directory = os.getcwd() + "\\images\\ds_18\\"
        for file in os.listdir(directory):
            if file.endswith(".jpg") and os.path.join(directory, file).replace('.','\\').split("\\")[-2].replace('-', '') in model_name.replace('-', ''):
                return os.path.join(directory, file)

        print("Did not find image for %s." % model_name)


    @staticmethod
    def add_new_product(ds18_variant):
        """
        Method that adds a new Wheel Pros Tire to Shopify
        :param ds18_variant: Tire to add:
        :return: Returns nothing
        """
        # TODO: Need to find a way to stream line this
        # TODO: Comment out the method
        print(ds18_variant.get_model())

        # Make the tags that we want to add
        tags_to_add = []
        # Brand
        tags_to_add.append("Brand_" + ds18_variant.get_collection())

        # 2 cases
        # 1) Is a variant
        if ds18Tools.has_variants(ds18_variant):
            return
            product_id = ds18Tools.find_product_id(ds18_variant)
            new_ds18_product = shopify.Product.find(product_id)
            variant = shopify.Variant({'price': float(ds18_variant.get_msrp_price()),
                                       'quantity': 1,
                                       'sku': ds18_variant.get_model(),
                                       'position': 1,
                                       'inventory_policy': 'continue',
                                       'fulfillment_service': 'manual',
                                       'inventory_management': 'shopify',
                                       'inventory_quantity': 1,
                                       'taxable': False,
                                       'weight_unit': 'g',
                                       'requires_shipping': True})
            # Get tags already put in
            tags = Tags()
            tags.string_to_tags(new_ds18_product.tags)
            # Now, we can go through and add the tags we want
            for t in tags_to_add:
                if not tags.is_a_tag(t) and "nan" not in t:
                    tags.add_tag(t)

            new_ds18_product.tags = tags.tags_to_string()

            new_ds18_product.tags = tags.tags_to_string()
            new_ds18_product.variants.append(variant)
            new_ds18_product.save()
            ds18Tools.add_product(product_id, ds18_variant)
            # 2) Is not a variant
        else:
            new_ds18_product = shopify.Product()
            # Built the tire name
            new_ds18_product.title = ds18_variant.get_name()
            new_ds18_product.vendor = 'DS 18'
            new_ds18_product.product_type = 'Sound'
            new_ds18_product.body_html = """<b>%s</b>
                                   <p>%s</p>
                                   """ % (ds18_variant.get_brand, ds18_variant.get_name())
            variant = shopify.Variant({'price': float(ds18_variant.get_msrp_price()),
                                       'quantity': 1,
                                       'sku': ds18_variant.get_model(),
                                       'position': 1,
                                       'inventory_policy': 'continue',
                                       'fulfillment_service': 'manual',
                                       'inventory_management': 'shopify',
                                       'inventory_quantity': 1,
                                       'taxable': False,
                                       'weight_unit': 'g',
                                       'requires_shipping': True})
            new_ds18_product.variants = [variant]

            new_ds18_product.tags = """DS18,
                       Sound"""

            # Get tags already put in
            tags = Tags()
            tags.string_to_tags(new_ds18_product.tags)
            # Now, we can go through and add the tags we want
            for t in tags_to_add:
                if not tags.is_a_tag(t) and "nan" not in t:
                    tags.add_tag(t)

            new_ds18_product.tags = tags.tags_to_string()

            image = shopify.Image()
            image.src = "https://ds18.s3.us-east-2.amazonaws.com/" + ds18_variant.get_model().replace("-", "").replace("/", "") + ".jpg"
            new_ds18_product.images = [image]

            ds18Tools.add_product(new_ds18_product.id, ds18_variant)
            new_ds18_product.save()  # returns false if the record is invalid
            if new_ds18_product.errors:
                # something went wrong, see new_product.errors.full_messages() for example
                new_ds18_product.errors.full_messages()

    @staticmethod
    def add_new_products(ds18_products):
        bar = pyprind.ProgBar(len(ds18_products), monitor=True, update_interval=.1)
        total_added = 1
        for t in range(len(ds18_products)):
            try:
                ShopifyToolsDS18.add_new_product(ds18_products[t])
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
    def update_product(ds18_variant):
        pass

    @staticmethod
    def update_products(ds18_products):
        pass

    @staticmethod
    def delete_product(ds18_variant):
        pass

    @staticmethod
    def delete_products(ds18_products):
        pass

    @staticmethod
    def get_all_ds18_variants_skus_from_shopify():
        pass

    @staticmethod
    def get_all_ds18_variants_in_shopify():
        pass

#---------------------------------
#--Methods to run the program
#---------------------------------

def add_ds18_products_shopify_tool():
    ds18_info = ExcelTools.read_ds18(r'sheets/ds18/12-20-2019_ds18_products.xlsx')
    ShopifyToolsDS18.add_new_products(ds18_info)

def update_ds18_products_shopify_tool():
    pass

def delete_ds18_products_shopify_tool():
    pass

add_ds18_products_shopify_tool()
