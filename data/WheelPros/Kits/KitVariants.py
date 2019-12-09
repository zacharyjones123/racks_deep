class KitVariants:
    def __init__(self, upc, kit_name, wheel, tire, msrp, size):
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
        self.kit_name_overflow = kit_name + " - " + wheel
        self.wheel = wheel
        self.tire = tire
        self.msrp = msrp
        self.size = size

    def get_upc(self):
        """
        Getter method for upc variable
        :return: upc
        """
        return self.upc
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

    def get_msrp(self):
        """
        Getter method for msrp variable
        :return: msrp
        """
        return self.msrp

    def get_size(self):
        """
        Getter method for size variable
        :return: size of wheel
        """
        return self.size

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
