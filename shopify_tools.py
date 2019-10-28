import shopify
from cred.cred import SHOP_URL
import pyprind
from urllib.error import HTTPError
import time

from data.TireTools import TireTools
from data.WheelTools import WheelTools
from excel_tools import ExcelTools

wheelTools = WheelTools()
tireTools = TireTools()


class ShopifyTools:

    @staticmethod
    def start_shopify_api():
        shopify.ShopifyResource.set_site(SHOP_URL)
        return shopify.Shop.current

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
        success = update_product.save()  # returns false if the record is invalid
        # or
        if update_product.errors:
            # something went wrong, see new_product.errors.full_messages() for example
            update_product.errors.full_messages()

    # Products - run 40 secs average
    @staticmethod
    def get_all_product_ids(resource, **kwargs):
        """
        Method that will return all of the product resources

        :param resource: shopify.Product (I can probably expand this)
        :param kwargs: Other options to filter
        :return: a list of all resources
        """
        print("Getting All Product Ids:")
        resource_count = resource.count(**kwargs)
        resources = []
        if resource_count > 0:
            bar = pyprind.ProgBar(len(range(1, ((resource_count - 1) // 250) + 2)), monitor=True)
            for page in range(1, ((resource_count - 1) // 250) + 2):
                #time.sleep(0.25)
                kwargs.update({"limit": 250, "page": page})
                resources.extend(resource.find(**kwargs))
                bar.update()
        return resources

    @staticmethod
    def product_ids_to_products(resources):
        product_dict = {}
        for r in resources:
            product_dict[r.id] = r
        return product_dict

    # urllib.error.HTTPError: HTTP Error 500: Internal Server Error
    # TimeoutError: [WinError 10060] A connection attempt failed because the connected party did not properly respond after a period of time, or established connection failed because connected host has failed to respond
    @staticmethod
    def add_new_wheel(wheel_variant):
        # 2 cases
        # 1) Is a variant
        if wheelTools.has_variants(wheel_variant):
            product_id = wheelTools.find_product_id(wheel_variant)
            new_wheel_product = shopify.Product.find(product_id)
            variant = shopify.Variant({'price': float(wheel_variant.get_map_price()),
                                       'option1': wheel_variant.get_size(),
                                       'option2': wheel_variant.get_offset(),
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
            #print(new_wheel_product)
            new_wheel_product.variants.append(variant)
            # print("Variants: ", new_wheel_product.variants)
            new_wheel_product.save()
            wheelTools.add_wheel(product_id, wheel_variant)
        # 2) Is not a variant
        else:
            # Update a product
            new_wheel_product = shopify.Product()
            new_wheel_product.options = [{'name': 'Tire Size'}, {'name': 'Offset'}]
            new_wheel_product.title = wheel_variant.get_style_description()
            new_wheel_product.vendor = "Wheel Pros"
            new_wheel_product.product_type = "Wheels"
            new_wheel_product.body_html = """<b>%s</b>
                                    <p>%s</p>
                                    """ % (wheel_variant.get_style_description(), wheel_variant.get_part_num_description())
            variant = shopify.Variant({'price': float(wheel_variant.get_map_price()),
                                       'option1': wheel_variant.get_size(),
                                       'option2': wheel_variant.get_offset(),
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
            new_wheel_product.tags = """WheelPros,
                        Wheels,
                        %s, 
                        %s,
                        %s,
                        %s,
                        %s""" % (wheel_variant.get_part_number(), wheel_variant.get_size(), wheel_variant.get_finish(), wheel_variant.get_offset(), wheel_variant.get_upc())

            image = shopify.Image()
            file_name = "%s" % (wheel_variant.get_wheel_image())
            image.src = file_name
            new_wheel_product.images = [image]
            new_wheel_product.save()

            wheelTools.add_wheel(new_wheel_product.id, wheel_variant)

            #print("PRODUCT ID: ", new_wheel_product.id)
            success = new_wheel_product.save()  # returns false if the record is invalid
            # or
            if new_wheel_product.errors:
                # something went wrong, see new_product.errors.full_messages() for example
                new_wheel_product.errors.full_messages()

    @staticmethod
    def add_new_wheels(wheels):
        bar = pyprind.ProgBar(len(wheels), monitor=True, update_interval=.1)
        total_added = 1
        for i in range(len(wheels)):
            try:
                w = wheels[i]
                # print("adding: ", w.get_style_description())
                ShopifyTools.add_new_wheel(w)
                bar.update(item_id=str(total_added))
                total_added +=1
            except TimeoutError:
                total_added -= 1
                print("Timeout error has occured, restarting server in 5 seconds")
                time.sleep(10)
            except HTTPError:
                total_added -= 1
                print("HTTP error has occured, restarting server in 5 seconds")
                time.sleep(10)


    @staticmethod
    def add_new_tires(tires):
        bar = pyprind.ProgBar(len(tires), monitor=True, update_interval=.1)
        total_added = 1
        for t in tires:
            ShopifyTools.add_new_tire(t)
            bar.update(item_id=str(total_added))
            total_added += 1
    @staticmethod
    def find_tire_brand(tire_description):
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

    # urllib.error.HTTPError: HTTP Error 500: Internal Server Error
    @staticmethod
    def add_new_tire(tire_variant):
        # 2 cases
        # 1) Is a variant
        #print(tire_variant.get_comparison_var())
        if tireTools.has_variants(tire_variant):
            product_id = tireTools.find_product_id(tire_variant)
            new_tire_product = shopify.Product.find(product_id)
            variant = shopify.Variant({'price': float(tire_variant.get_map_price()),
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
            new_tire_product.variants.append(variant)
            new_tire_product.save()
            tireTools.add_tire(product_id, tire_variant)
            # 2) Is not a variant
        else:
            new_tire_product = shopify.Product()
            new_tire_product.options = [{'name': 'Tire Size'}]
            new_tire_product.title = tire_variant.get_tire_description()
            new_tire_product.vendor = 'Wheel Pros'
            new_tire_product.product_type = 'Tires'
            new_tire_product.body_html = """<b>%s</b>
                                   <p>%s</p>
                                   """ % (tire_variant.get_tire_description(), tire_variant.get_part_num())
            variant = shopify.Variant({'price': float(tire_variant.get_map_price()),
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

            image = shopify.Image()
            file_name = "https://images.wheelpros.com/h%s.png" % (tire_variant.get_picture_cd())
            image.src = file_name
            new_tire_product.images = [image]
            new_tire_product.save()

            tireTools.add_tire(new_tire_product.id, tire_variant)
            success = new_tire_product.save()  # returns false if the record is invalid
            # or
            if new_tire_product.errors:
                # something went wrong, see new_product.errors.full_messages() for example
                new_tire_product.errors.full_messages()


    @staticmethod
    def delete_products(products):
        # DONE
        # 00:02:05 - TIRES
        # HTTP 404 error - not found
        # HTTP 429 error - too many request - Just need to pause and let the bucket leak (Leaky Bucket Algorithm)
        # Shopify PLus
        # Bucket Size: 80
        # Leak Rate:   4/second
        print("Deleting Products:")
        bar = pyprind.ProgBar(len(products), monitor=True, update_interval=.1)
        print("Started")
        print(len(products))
        total_deleted = 0
        for p in products:
            # Get the specific product
            id_for_product = wheelTools.find_id(p)
            if id_for_product is not None:
                # print(id_for_product)
                deletes_product = shopify.Product.find(id_for_product)
                # Remove the product
                deletes_product.destroy()
                wheelTools.delete_wheel(id_for_product)
                total_deleted += 1
            bar.update(item_id=str(total_deleted))
        print(bar)


shop = ShopifyTools.start_shopify_api()

# Makes a dictionary of product_ids to the actual resource
# great for checking if the certain Product makes the resource
ShopifyTools.add_new_wheels(ExcelTools.read_product_technical_data_usd(r'sheets/exp_10-21-2019_producttechdatausd.xlsx'))
#ShopifyTools.add_new_tires(ExcelTools.read_tire_data_usd(r'sheets/exp_10-21-2019_tireData.xlsx'))

