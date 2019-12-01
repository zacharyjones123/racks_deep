"""
WheelVariants class
- represents Wheel Pros Wheels products
"""


class WheelVariants:
    def __init__(self, style_description, part_number, part_num_description,
                 size, finish, map_price, offset, upc,
                 ship_weight, wheel_image, bolt_pattern_metric, bolt_pattern_us,
                 msrp_price, lug_count, bolt_pattern_mm1, bolt_pattern_mm2):
        """
        Init method for WheelVariants Object
        :param style_description: Title of the wheel product
        :param part_number: Part Number
        :param part_num_description: Part Number
        :param size: Size of the wheel
        :param finish: finish on the wheel
        :param map_price: M.A.P. Price
        :param offset: Offset of the wheel
        :param upc: UPC Code
        :param ship_weight: Shipping Weight
        :param wheel_image: URL image of the wheel
        :param bolt_pattern_metric: metric bolt_pattern
        :param bolt_pattern_us: us bolt_pattern
        :param msrp_price: M.S.R.P. price
        :param lug_count: Number of lugs
        :param bolt_pattern_mm1: first bolt pattern
        :param bolt_pattern_mm2: second bolt pattern
        """
        self.style_description = style_description
        self.part_number = part_number
        self.part_num_description = part_num_description
        self.size = size
        self.finish = finish
        self.map_price = map_price
        self.offset = offset
        self.upc = upc
        self.ship_weight = ship_weight
        self.wheel_image = wheel_image
        self.bolt_pattern_metric = bolt_pattern_metric
        self.bolt_pattern_us = bolt_pattern_us
        self.msrp_price = msrp_price
        self.lug_count = lug_count
        self.bolt_pattern_mm1 = bolt_pattern_mm1
        self.bolt_pattern_mm2 = bolt_pattern_mm2

    def get_style_description(self):
        """
        Getter method for style_description
        :return: style_description
        """
        return self.style_description

    def get_part_number(self):
        """
        Getter method for part_number
        :return: part_number
        """
        return self.part_number

    def get_part_num_description(self):
        """
        Getter method for part_num_description
        :return: part_num_description
        """
        return self.part_num_description

    def get_size(self):
        """
        Getter method for size
        :return: size
        """
        return self.size

    def get_finish(self):
        """
        Getter method for finish
        :return: finish
        """
        return self.finish

    def get_map_price(self):
        """
        Getter method for map_price
        :return: map_price
        """
        return self.map_price

    def get_offset(self):
        """
        Getter method for offset
        :return: offset
        """
        return self.offset

    def get_upc(self):
        """
        Getter method for upc
        :return: upc
        """
        return self.upc

    def get_ship_weight(self):
        """
        Getter method for ship_weight
        :return: ship_weight
        """
        return self.ship_weight

    def get_wheel_image(self):
        """
        Getter method for wheel_image
        :return: wheel_image
        """
        return self.wheel_image
    
    def get_bolt_pattern_metric(self):
        """
        Getter method for bolt_pattern_metric
        :return: bolt_pattern_metric
        """
        return self.bolt_pattern_metric
    
    def get_bolt_pattern_us(self):
        """
        Getter method for bolt_pattern_us
        :return: bolt_pattern_us
        """
        return self.bolt_pattern_us

    def get_msrp_price(self):
        """
        Getter method for msrp_price
        :return: msrp_price
        """
        return self.msrp_price

    def get_lug_count(self):
        """
        Getter method for lug_count
        :return: lug_count
        """
        return self.lug_count

    def get_bolt_pattern_mm1(self):
        """
        Getter method for bolt_pattern_mm1
        :return: bolt_pattern_mm1
        """
        return self.bolt_pattern_mm1

    def get_bolt_pattern_mm2(self):
        """
        Getter method for bolt_pattern_mm2
        :return: bolt_pattern_mm2
        """
        return self.bolt_pattern_mm2

    def __eq__(self, o) -> bool:
        """
        Equality method for WheelVariants
        The method goes through and compares all of the
        elements directly
        :param o: other WheelVariant
        :return: If the 2 are the same
        """
        if self.get_style_description() != o.get_style_description():
            return False
        if self.get_part_number() != o.get_part_number():
            return False
        if self.get_part_num_description() != o.get_part_num_description():
            return False
        if self.get_size() != o.get_size():
            return False
        if self.get_finish() != o.get_finish():
            return False
        if self.get_map_price() != o.get_map_price():
            return False
        if self.get_offset() != o.get_offset():
            return False
        if self.get_upc() != o.get_upc():
            return False
        if self.get_ship_weight() != o.get_ship_weight():
            return False
        if self.get_wheel_image() != o.get_wheel_image():
            return False
        if self.get_bolt_pattern_metric() != o.get_bolt_pattern_metric():
            return False
        if self.get_bolt_pattern_us() != o.get_bolt_pattern_us():
            return False
        if self.get_msrp_price() != o.get_msrp_price():
            return False
        if self.get_lug_count() != o.get_lug_count():
            return False
        if self.get_bolt_pattern_mm1() != o.get_bolt_pattern_mm1():
            return False
        if self.get_bolt_pattern_mm2() != o.get_bolt_pattern_mm2():
            return False
        return True

    def compare_map_prices(self, o):
        """
        Compares 2 WheelVariant's map_prices
        :param o: Other WheelVariant
        :return: -1 -> self is more, 0 -> self is the same, 1 -> o is more
        """
        if self.get_map_price() < o.get_map_price():
            return -1
        elif self.get_map_price() == o.get_map_price():
            return 0
        else:
            return 1

    def compare_msrp_prices(self, o):
        """
        Compares 2 WheelVariant's msrp_prices
        :param o: Other Wheel Variant
        :return: -1 -> self is more, 0 -> self is the same, 1 -> o is more
        """
        if self.get_msrp_price() < o.get_msrp_price():
            return -1
        elif self.get_msrp_price() == o.get_msrp_price():
            return 0
        else:
            return 1

    def __str__(self):
        """
        Str representation of the WheelVariant
        :return:
        """
        return """%s,""" % (self.get_style_description())

    def __repr__(self):
        """
        Repr representation of WheelVariant
        :return:
        """
        return "Wheel Repr"
