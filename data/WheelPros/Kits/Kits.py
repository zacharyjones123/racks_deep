from data.WheelPros.Product import Products


class Kits(Products):
    def __init__(self, kit_variant):
        """
        Init method for the Kits class
        :param kit_variant: starting kit_variant
        """
        super().__init__(kit_variant.get_wheel(), kit_variant.get_tire(), kit_variant.get_map_price())
        self.kit_variants = {kit_variant.get_upc(): kit_variant}
        self.product_id = None

    def get_kit_variants(self):
        """
        Getter method for kit variants list
        :return: kit variants list
        """
        return self.kit_variants

    def add_kit_variant(self, kit_variant):
        """
        Method to add a new kit variant to the kit variants dictionary
        :param kit_variant: new kit_variant to add
        :return: Nothing
        """
        self.kit_variants[kit_variant.get_upc()] = kit_variant

    def set_product_id(self, product_id):
        """
        Setter method for product_id
        :param product_id: new product id
        :return: Nothing
        """
        self.product_id = product_id

    # Done
    def get_product_id(self):
        """
        Getter method for product_id
        :return: product_id
        """
        return self.product_id
