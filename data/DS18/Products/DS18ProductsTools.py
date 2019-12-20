from data.DS18.Products.DS18Products import DS18Products


class DS18ProductsTools:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, ds18_variant):
        if product_id not in self.products:
            self.products[product_id] = DS18Products(ds18_variant)
        else:
            self.products[product_id].add_variant(ds18_variant)

    def delete_product(self, product_id):
        del self.products[product_id]

    def get_products(self):
        return self.products

    def find_product_id(self, ds18_variant):
        for product_id in self.products:
            if ds18_variant.get_name() == self.products[product_id].get_name():
                return product_id
        return None

    def has_variants(self, ds18_variant):
        for product_id in self.products:
            if ds18_variant.get_name() == self.products[product_id].get_name():
                return True
        return False
