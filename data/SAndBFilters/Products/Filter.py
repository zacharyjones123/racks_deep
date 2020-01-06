class Filter():
    def __init__(self, filter_variant):
        self.variants = {filter_variant.get_part_num(): filter_variant}
        self.product_id = None
        self.prod_fit = filter_variant.get_prod_fit()

    def get_prod_fit(self):
        return self.prod_fit

    def add_variant(self, filter_variant):
        self.variants[filter_variant.get_part_num()] = filter_variant

    def get_variants(self):
        return self.variants

    def set_product_id(self, product_id):
        self.product_id = product_id

    def get_product_id(self):
        return self.product_id