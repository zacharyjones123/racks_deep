from data.WheelPros.Product import Products


class Wheels(Products):
    # Done
    def __init__(self, wheel_variant):
        super().__init__(wheel_variant.upc, wheel_variant.map_price)
        self.variants = {wheel_variant.upc: wheel_variant}
        self.product_id = None

        self.style_description = wheel_variant.style_description

    # Done
    def get_style_description(self):
        return self.style_description

    # Done
    def add_variant(self, variant_wheel):
        self.variants[variant_wheel.upc] = variant_wheel

    # Done
    def get_variants(self):
        return self.variants

    # Done
    def set_product_id(self, product_id):
        self.product_id = product_id

    # Done
    def get_product_id(self):
        return self.product_id
