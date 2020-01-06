"""
Class Representation of S&B Filters Products
"""


class FilterVariant:
    def __init__(self, part_num, upc, prod_description, prod_fit, veh_type, map_price):
        """
        Init Method for Filter
        :param part_num: part number
        :param upc: upc
        :param prod_description: product description
        :param prod_fit: product fitment
        :param veh_type: vehicle type
        :param map_price: map price
        """
        self.part_num = part_num
        self.upc = upc
        self.prod_description = prod_description
        self.prod_fit = prod_fit
        self.veh_type = veh_type
        self.map_price = map_price

    def get_part_num(self):
        """
        Getter method for part_num
        :return: part_num
        """
        return self.part_num

    def get_upc(self):
        """
        Getter method for upc
        :return: upc
        """
        return self.upc

    def get_prod_description(self):
        """
        Getter method for prod_description
        :return: prod_description
        """
        return self.prod_description

    def get_prod_fit(self):
        """
        Getter method for prod_fit
        :return: prod_fit
        """
        return self.prod_fit

    def get_veh_type(self):
        """
        Getter method for veh_type
        :return: veh_type
        """
        return self.veh_type

    def get_map_price(self):
        """
        Getter method for map_price
        :return: map_price
        """
        return self.map_price

    def __str__(self):
        """
        Str method for Filter
        :return: str represetnation
        """
        return "S&B Filter Product"

    def __repr__(self):
        """
        Repr Method for Filter
        :return: repr representation
        """
        return "S&B Filter Repr"
