class KitVariants:
    def __init__(self, upc, kit_name, wheel, tire, price):
        """
        Init method for Kits class
        :param upc: upc
        :param kit_name: Kit Name
        :param wheel: wheel_name
        :param tire: tire_name
        :param map_price: price of the kit
        """
        self.upc = upc
        self.kit_name = kit_name
        self.wheel = wheel
        self.tire = tire
        self.price = price

    def get_upc(self):
        """
        Getter method for upc variable
        :return: upc
        """
    def get_kit_name(self):
        """
        Getter method for kit_name variable
        :return: kit_name
        """
        return self.kit_name

    def get_wheel(self):
        """
        Getter method for wheel variable
        :return: wheel
        """
        return self.wheel

    def get_tire(self):
        """
        Getter method for tire variable
        :return: tire
        """
        return self.tire

    def get_price(self):
        """
        Getter method for map_price variable
        :return: map_price
        """
        return self.price

    def __str__(self):
        """
        Str method for Kits
        :return: Str representation for Kits
        """
        return "Kit Display Text"

    def __repr__(self):
        """
        Repr method for Kits
        :return: repr representation of Kits
        """
        return "Kit Repr"
