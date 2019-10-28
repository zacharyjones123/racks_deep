from data.Tires import Tires


class TireTools:
    # Done
    def __init__(self):
        self.tires = {}

    # Done
    def add_tire(self, product_id, tire_variant):
        if product_id not in self.tires:
            self.tires[product_id] = Tires(tire_variant)
        else:
            self.tires[product_id].add_variant(tire_variant)

    # Done
    def delete_tire(self, product_id):
        del self.tires[product_id]

    # Done
    def get_tires(self):
        return self.tires

    def find_product_id(self, tire_variant):
        for product_id in self.tires:
            if tire_variant.get_comparison_var() == self.tires[product_id].get_comparison_var():
                return product_id
        return None

    def has_variants(self, tire_variant):
        for product_id in self.tires:
            #print("--------------")
            #print(tire_variant.get_comparison_var())
            #print(self.tires[product_id].get_comparison_var())
            if tire_variant.get_comparison_var() == self.tires[product_id].get_comparison_var():
                return True
        return False
