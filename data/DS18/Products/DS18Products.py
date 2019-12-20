class DS18Products():
    def __init__(self, ds18_variant):
        self.variants = {ds18_variant.get_model(): ds18_variant}
        self.product_id = None
        self.name = ds18_variant.get_name()

    def get_name(self):
        return self.name

    def add_variant(self, ds18_variant):
        self.variants[ds18_variant.get_model()] = ds18_variant

    def get_variants(self):
        return self.variants

    def set_product_id(self, product_id):
        self.product_id = product_id

    def get_product_id(self):
        return self.product_id