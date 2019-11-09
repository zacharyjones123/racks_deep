class Vehicles:
    def __init__(self, make, model, year):
        """
        Init method for Vehicles class
        :param make: make of the vehicle
        :param model: model of the vehicle
        :param year: year of the vehicle
        """
        self.make = make
        self.model = model
        self.year = year

    def get_make(self):
        """
        Getter method for make variable
        :return: make
        """
        return self.make

    def get_model(self):
        """
        Getter method for model variable
        :return: model
        """
        return self.model

    def get_year(self):
        """
        Getter method for year variable
        :return: year
        """
        return self.year

    def set_make(self, make):
        """
        Setter method for make variable
        :param make: new make
        :return: Nothing
        """
        self.make = make

    def set_model(self, model):
        """
        Setter method for model variable
        :param model: new model
        :return: Nothing
        """
        self.model = model

    def set_year(self, year):
        """
        Setter method for year variable
        :param year: new year
        :return: Nothing
        """
        self.year = year

    def __str__(self):
        """
        Str method for Vehicles
        :return: Str representation
        """
        return "Vehicles Str Representation"

    def __repr__(self):
        """
        Repr method for Vehicle
        :return: Repr representation
        """
        return "Vehicles Repr"
