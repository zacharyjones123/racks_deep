from data.WheelPros.Product import Products


class Kits(Products):
    def __init__(self, kit_variant):
        """
        Init method for the Kits class
        :param kit_variant: starting kit_variant
        """
        super().__init__(kit_variant.get_upc(), kit_variant.get_msrp())
        self.kit_variants = {kit_variant.get_upc(): kit_variant}
        self.product_id = None
        self.kit_name = kit_variant.get_kit_name()

    def get_kit_name(self):
        return self.kit_name

    # Done
    def add_variant(self, variant_kit):
        self.kit_variants[variant_kit.get_upc()] = variant_kit

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
