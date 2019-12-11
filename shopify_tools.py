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

from excel_tools import ExcelTools


import mimetypes


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
        return product_dicte

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


shop = ShopifyTools.start_shopify_api()
# This is all of the products, so we can
product_dict = ShopifyTools.product_ids_to_products(ShopifyTools.get_all_product_ids(shopify.Product))