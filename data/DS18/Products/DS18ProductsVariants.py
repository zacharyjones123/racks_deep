class DS18Variants:
    def __init__(self,
                 model,
                 brand,
                 name,
                 m_c,
                 msrp_price,
                 dealer_price,
                 collection):
        self.model = model
        self.brand = brand
        self.name = name
        self.m_c = m_c
        self.msrp_price = msrp_price
        self.dealer_price = dealer_price
        self.collection = collection

    def set_model(self, model):
        self.model = model

    def set_brand(self, brand):
        self.brand = brand

    def set_name(self, name):
        self.name = name

    def set_m_c(self, m_c):
        self.m_c = m_c

    def set_msrp_price(self, msrp_price):
        self.msrp_price = msrp_price

    def set_dealer_price(self, dealer_price):
        self.dealer_price = dealer_price

    def set_collection(self, collection):
        self.collection = collection

    def get_model(self):
        return self.model

    def get_brand(self):
        return self.brand

    def get_name(self):
        return self.name

    def get_m_c(self):
        return self.m_c

    def get_msrp_price(self):
        return self.msrp_price

    def get_dealer_price(self):
        return self.dealer_price

    def get_collection(self):
        return self.collection

    def __eq__(self, o) -> bool:
        pass

    def __str__(self) -> str:
        return self.get_model() + " - " + self.get_name()

    def __repr__(self) -> str:
        return super().__repr__()