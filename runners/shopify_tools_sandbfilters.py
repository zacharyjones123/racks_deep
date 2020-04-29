import time

import pyactiveresource
import pyprind

import urllib.request

from sheets.SAndBFilters.read_s_and_b_filters_csv import get_filters_from_asap
from data.SAndBFilters.Products.FilterTools import FilterTools
from data.WheelPros.Tags import Tags
from urllib.error import HTTPError
import shopify

# S&B Filter - Local Storage for S&B Filters
filterTools = FilterTools()


class ShopifyToolsFilter:

    @staticmethod
    def url_is_alive(url):
        """
        Checks that a given URL is reachable.
        :param url: A URL
        :rtype: bool
        """
        request = urllib.request.Request(url)
        request.get_method = lambda: 'HEAD'

        try:
            urllib.request.urlopen(request)
            return True
        except urllib.request.HTTPError:
            return False

    @staticmethod
    def add_new_product(filter_variant):
        """
        Method that adds a new Wheel Pros Tire to Shopify
        :param ds18_variant: Tire to add:
        :return: Returns nothing
        """
        # TODO: Need to find a way to stream line this
        # TODO: Comment out the method

        # Make the tags that we want to add
        tags_to_add = []
        # Brand
        #print(filter_variant)
        tags_to_add.append("Type_" + str(filter_variant.get_prod_description()))

        # 2 cases
        # 1) Is a variant
        print(filter_variant)
        if filterTools.has_variants(filter_variant):
            product_id = filterTools.find_product_id(filter_variant)
            new_filter_product = shopify.Product.find(product_id)[0]
            print("Type of new_filter_project: ", type(new_filter_product))
            variant = shopify.Variant({'price': float(filter_variant.get_map_price()),
                                       'quantity': 1,
                                       'sku': filter_variant.get_upc(),
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
            print("Type of new_filter_project: ",type(new_filter_product))
            tags.string_to_tags(new_filter_product.tags)
            # Now, we can go through and add the tags we want
            for t in tags_to_add:
                if not tags.is_a_tag(t) and "nan" not in t:
                    tags.add_tag(t)

            new_filter_product.tags = tags.tags_to_string()

            new_filter_product.tags = tags.tags_to_string()
            new_filter_product.variants.append(variant)
            new_filter_product.save()
            if new_filter_product.errors:
                # something went wrong, see new_product.errors.full_messages() for example
                new_filter_product.errors.full_messages()
            filterTools.add_product(product_id, filter_variant)
            # 2) Is not a variant
        else:
            print(filter_variant)
            new_filter_product = shopify.Product()
            # Built the tire name
            new_filter_product.title = filter_variant.get_prod_description()
            new_filter_product.vendor = 'S&B Filters'
            new_filter_product.product_type = 'Filters'
            new_filter_product.body_html = """%s
                                   """ % (filter_variant.get_prod_description())
            variant = shopify.Variant({'price': float(filter_variant.get_map_price()),
                                       'quantity': 1,
                                       'sku': filter_variant.get_upc(),
                                       'position': 1,
                                       'inventory_policy': 'continue',
                                       'fulfillment_service': 'manual',
                                       'inventory_management': 'shopify',
                                       'inventory_quantity': 1,
                                       'taxable': False,
                                       'weight_unit': 'g',
                                       'requires_shipping': True})
            new_filter_product.variants = [variant]

            new_filter_product.tags = """S&B Filters,
                       Filters"""

            # Get tags already put in
            tags = Tags()
            tags.string_to_tags(new_filter_product.tags)
            # Now, we can go through and add the tags we want
            for t in tags_to_add:
                if not tags.is_a_tag(t) and "nan" not in t:
                    tags.add_tag(t)

            new_filter_product.tags = tags.tags_to_string()

            url_for_image = filter_variant.get_image_url().split("|")[0]
            print("The image: ",url_for_image)

           # if not ShopifyToolsFilter.url_is_alive(url_for_image):
            #    url_for_image = "https://sandbfilters.s3.us-east-2.amazonaws.com/" + filter_variant.get_part_num() + ".png"

            image = shopify.Image()
            image.src = url_for_image
            new_filter_product.images = [image]

            filterTools.add_product(new_filter_product.id, filter_variant)
            new_filter_product.save()  # returns false if the record is invalid
            if new_filter_product.errors:
                print("Hello")
                # something went wrong, see new_product.errors.full_messages() for example
                new_filter_product.errors.full_messages()

    @staticmethod
    def add_new_products(filter_products):
        bar = pyprind.ProgBar(len(filter_products), monitor=True, update_interval=.1)
        total_added = 1
        for t in range(len(filter_products)):
            try:
                ShopifyToolsFilter.add_new_product(filter_products[t])
                bar.update(item_id=str(total_added))
                total_added += 1
            except pyactiveresource.connection.Error as err:
                print(err)
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

def add_filter_products_shopify_tool():
    #filter_info = ExcelTools.read_s_and_b_filters(r'sheets/SAndBFilters/sAndBFilters_prices.xlsx')
    filter_info = get_filters_from_asap()
    ShopifyToolsFilter.add_new_products(filter_info)

def update_s_and_b_filters_products_shopify_tool():
    pass

def delete_s_and_b_filters_products_shopify_tool():
    pass

add_filter_products_shopify_tool()
