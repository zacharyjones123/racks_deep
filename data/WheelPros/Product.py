class Products:
    def __init__(self, upc, map_price):
        self.upc = upc
        self.map_price = map_price

    def get_upc(self):
        return self.upc

    def get_map_price(self):
        return self.map_price

    def set_upc(self, upc):
        self.upc = upc

    def set_map_price(self, map_price):
        self.map_price = map_price
