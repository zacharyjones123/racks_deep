class WheelVariants:
    def __init__(self, style_description, part_number, part_num_description,
                 size, finish, map_price, offset, upc,
                 ship_weight, wheel_image, bolt_pattern_metric, bolt_pattern_us,
                 msrp_price):
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

    def get_style_description(self):
        return self.style_description

    def get_part_number(self):
        return self.part_number

    def get_part_num_description(self):
        return self.part_num_description

    def get_size(self):
        return self.size

    def get_finish(self):
        return self.finish

    def get_map_price(self):
        return self.map_price

    def get_offset(self):
        return self.offset

    def get_upc(self):
        return self.upc

    def get_ship_weight(self):
        return self.ship_weight

    def get_wheel_image(self):
        return self.wheel_image
    
    def get_bolt_pattern_metric(self):
        return self.bolt_pattern_metric
    
    def get_bolt_pattern_us(self):
        return self.bolt_pattern_us

    def get_msrp_price(self):
        return self.msrp_price

    def __eq__(self, o) -> bool:
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
        return True

    def compare_map_prices(self, o):
        if self.get_map_price() < o.get_map_price():
            return -1
        elif self.get_map_price() == o.get_map_price():
            return 0
        else:
            return 1

    def compare_msrp_prices(self, o):
        if self.get_msrp_price() < o.get_msrp_price():
            return -1
        elif self.get_msrp_price() == o.get_msrp_price():
            return 0
        else:
            return 1

    def __str__(self):
        return """%s,""" % (self.get_style_description())

    def __repr__(self):
        return "Wheel Repr"
