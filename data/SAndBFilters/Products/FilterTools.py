from data.SAndBFilters.Products.Filter import Filter


class FilterTools:
    def __init__(self):
        self.products = {}

    def add_product(self, product_id, filter_variant):
        if product_id not in self.products:
            self.products[product_id] = Filter(filter_variant)
        else:
            self.products[product_id].add_variant(filter_variant)

    def delete_product(self, product_id):
        del self.products[product_id]

    def get_products(self):
        return self.products

    def find_product_id(self, filter_variant):
        for product_id in self.products:
            if filter_variant.get_prod_fit() == self.products[product_id].get_prod_fit():
                return product_id
        return None

    def has_variants(self, filter_variant):
        for product_id in self.products:
            if filter_variant.get_prod_fit() == self.products[product_id].get_prod_fit():
                return True
        return False
