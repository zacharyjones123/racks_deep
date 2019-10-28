class TireVariants:
    def __init__(self, part_num, tire_size, tire_description, tire_size_description, upc, picture_cd, weight, map_price):
        self.upc = upc
        self.map_price = map_price
        self.part_num = part_num
        self.tire_size = tire_size
        self.tire_description = tire_description
        self.tire_size_description = tire_size_description
        self.picture_cd = picture_cd
        self.weight = weight
        self.comparison_var = None

    def get_comparison_var(self):
        return self.comparison_var

    def set_comparison_var(self, comparison_var):
        self.comparison_var = comparison_var

    def get_map_price(self):
        return self.map_price

    def get_part_num(self):
        return self.part_num

    def get_tire_size(self):
        return self.tire_size

    def get_tire_description(self):
        return self.tire_description

    def get_tire_size_description(self):
        return self.tire_size_description

    def get_upc(self):
        return self.upc

    def get_picture_cd(self):
        return self.picture_cd

    def get_weight(self):
        return self.weight

    def __eq__(self, o) -> bool:
        if self.get_part_num() != o.get_part_num():
            return False
        if self.get_tire_size() != o.get_tire_size():
            return False
        if self.get_tire_description() != o.get_tire_description():
            return False
        if self.get_tire_size_description() != o.get_tire_size_description():
            return False
        if self.get_upc() != o.get_upc():
            return False
        if self.get_picture_cd() != o.get_picture_cd():
            return False
        if self.get_weight() != o.get_weight():
            return False
        if self.get_map_price() != o.get_map_price():
            return False
        return True

    def __str__(self) -> str:
        return self.get_tire_description() + self.get_upc()

    def __repr__(self) -> str:
        return super().__repr__()