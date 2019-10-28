from data.Wheels import Wheels


class WheelTools:
    # Done
    def __init__(self):
        self.wheels = {}

    # Done
    def add_wheel(self, product_id, wheel_variant):
        if product_id not in self.wheels:
            self.wheels[product_id] = Wheels(wheel_variant)
        else:
            self.wheels[product_id].add_variant(wheel_variant)

    # Done
    def delete_wheel(self, product_id):
        del self.wheels[product_id]

    # Done
    def get_wheels(self):
        return self.wheels

    def find_product_id(self, wheel_variant):
        for product_id in self.wheels:
            if wheel_variant.get_style_description() == self.wheels[product_id].get_style_description():
                return product_id
        return None

    def has_variants(self, wheel_variant):
        for product_id in self.wheels:
            if wheel_variant.get_style_description() == self.wheels[product_id].get_style_description():
                return True
        return False
