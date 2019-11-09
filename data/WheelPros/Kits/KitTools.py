import pandas as pd
import pyprind

from data.WheelPros.Kits.Kits import Kits


def load_vehicles(spreadsheet_name):
    """
    Load Vehicles method to get all of the possible vehicles
    and fittings
    :param spreadsheet_name: name of the spreadsheet
    :return: Vehicles array
    """
    # TODO: Need to make this method for all of the wheel pros and what they fit to
    print(spreadsheet_name)
    return "Hello"


class KitTools:
    def __init__(self):
        """
        Init method for the KitTools object

        This method serves to init the:
        kits dictionary
        and the
        kits_variants_list list
        """
        self.kits = {}
        self.kit_variants_list = []
        self.vehicles = load_vehicles("spreadsheet_name")

    def load_kit_variants_from_file(self):
        print("Loading Save File")
        df = pd.read_excel(r'sheets/kits_save_file.xlsx')
        kit_variants_list = []
        all_total = 1
        bar = pyprind.ProgBar(len(df.index), monitor=True)
        for i in df.index:
            # TODO: Need to figure this out, the conversion
            # kit_variant = KitVariants()
            print(i)
            kit_variants_list.append(kit_variant)
            bar.update(item_id=all_total)
            all_total += 1
        self.kit_variants_list = kit_variants_list

    def save_kit_variants_to_file(self):
        print("Saving Save File")
        self.build.kit_variants_list()
        bar = pyprind.ProgBar(len(self.kit_variants_list), monitor=True)
        all_total = 1
        # df_temp = ?
        # TODO: From here down we need to figure out the save format

    def build_kits_variants_list(self):
        self.kit_variants_list = []
        for k in self.kits:
            for v in self.kits[k].get_variants():
                self.kit_variants_list.append(self.kits[k].get_variants()[k])

    def add_kit(self, product_id, kit_variant):
        if product_id not in self.kits:
            self.kits[product_id] = Kits(kit_variant)
            self.kits[product_id].set_product_id(product_id)
        else:
            self.wheels[product_id].add_variant(kit_variant)
            self.wheels[product_id].set_product_id(product_id)

    def delete_kit(self, product_id):
        self.kits[product_id]

    def set_kit_variants_list(self, kit_variants_list):
        self.kit_variants_list = kit_variants_list

    def get_kit_variants_list(self):
        return self.kit_variants_list

    def get_kits(self):
        return self.kits

    def find_product_id(self, kit_variant):
        for product_id in self.kits:
            pass
        # TODO: Need to figure out the style description part here
        # This is how we deterine if the products are the same or not

    def has_variants(self, kit_variant):
        for product_id in self.kits:
            pass
        # TODO: Need to figure out the style description part here
        # This is how we deterine if the products are the same or not
