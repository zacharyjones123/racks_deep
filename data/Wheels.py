from data.Product import Products


class Wheels(Products):
    # Done
    def __init__(self, wheel_variant):
        super().__init__(wheel_variant.get_upc(), wheel_variant.get_map_price())
        self.variants = {wheel_variant.get_upc(): wheel_variant}
        self.product_id = None

        self.style_description = wheel_variant.get_style_description()

    # Done
    def get_style_description(self):
        return self.style_description

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
