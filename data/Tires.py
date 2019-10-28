from data.Product import Products


class Tires(Products):
    # Done
    def __init__(self, tire_variant):
        super().__init__(tire_variant.get_upc(), tire_variant.get_map_price())
        self.variants = {tire_variant.get_upc(): tire_variant}
        self.product_id = None
        self.comparison_var_tires_copy = tire_variant.get_comparison_var()

    def get_comparison_var(self):
        return self.comparison_var_tires_copy

    # Done
    def add_variant(self, variant_wheel):
        self.variants[variant_wheel.get_upc()] = variant_wheel

    # Done
    def get_variants(self):
        return self.variants

    # Done
    def set_product_id(self, product_id):
        self.product_id = product_id

    # Done
    def get_product_id(self):
        return self.product_id
