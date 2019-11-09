class KitVariants:
    def __init__(self, wheel, tire, map_price, upc):
        """
        Init method for Kits class
        :param wheel: Wheels object for Kit
        :param tire: Tires object for Kit
        :param map_price: price of the kit
        :param upc: upc of the kit
        """
        self.wheel = wheel
        self.tire = tire
        self.map_price = map_price
        self.upc = upc

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

    def get_map_price(self):
        """
        Getter method for map_price variable
        :return: map_price
        """
        return self.map_price

    def get_upc(self):
        """
        Getter method for the upc variable
        :return: upc
        """
        return self.upc

    def set_wheel(self, wheel):
        """
        Setter method for wheel variable
        :param wheel: new wheel
        :return: Nothing
        """
        self.wheel = wheel

    def set_tire(self, tire):
        """
        Setter method for tire variable
        :param tire: new tire
        :return: Nothing
        """
        self.tire = tire

    def set_map_price(self, map_price):
        """
        Setter method for map_price variable
        :param map_price: new map_price
        :return: Nothing
        """
        self.map_price = map_price

    def set_upc(self, upc):
        """
        Setter method for the upc variable
        :param upc: new upc
        :return: Nothing
        """
        self.upc = upc

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
