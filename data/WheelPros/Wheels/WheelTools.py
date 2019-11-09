from data.WheelPros.Wheels.WheelVariants import WheelVariants
from data.WheelPros.Wheels.Wheels import Wheels
import pandas as pd
import pyprind
import pickle


class WheelTools:
    # Done
    def __init__(self):
        # wheels is the shopify side, with all of the
        # products on the server
        self.wheels = {}
        # wheel variants list is a list that is kept on file,
        # locally with load_file and save_file
        self.wheel_variants_list = []

    def load_wheel_variants_from_file(self):
        print("Loading Save File")
        df = pd.read_excel(r'sheets/save_files/save_file.xlsx')
        wheel_variants_list = []
        all_total = 1
        bar = pyprind.ProgBar(len(df.index), monitor=True)
        for i in df.index:
            wheel_variant = WheelVariants(str(df['styledescription'][i]),
                                  str(df['partnumber'][i]),
                                  str(df['partnumberdescription'][i]),
                                  str(df['size'][i]),
                                  str(df['finish'][i]),
                                  str(df['MapPrice'][i]),
                                  str(df['offset'][i]),
                                  str(int(df['upc'][i])),
                                  str(df['Shipping Weight'][i]),
                                  str(df['wheelimage'][i]))
            wheel_variants_list.append(wheel_variant)
            bar.update(item_id=all_total)
            all_total += 1
        self.wheel_variants_list = wheel_variants_list
        # self.build_wheels()

    def save_wheel_variants_to_file(self):
        print("Saving Save File")
        self.build_wheel_variants_list()
        bar = pyprind.ProgBar(len(self.wheel_variants_list), monitor=True)
        all_total = 1
        df_temp = {'styledescription': [],
                      'partnumber': [],
                      'partnumberdescription': [],
                      'size': [],
                      'finish': [],
                      'MapPrice': [],
                      'offset': [],
                      'upc': [],
                      'Shipping Weight': [],
                      'wheelimage': []}

        for w in self.wheel_variants_list:
            df_temp['styledescription'].append(w.get_style_description())
            df_temp['partnumber'].append(w.get_part_number())
            df_temp['partnumberdescription'].append(w.get_part_num_description())
            df_temp['size'].append(w.get_size())
            df_temp['finish'].append(w.get_finish())
            df_temp['MapPrice'].append(w.get_map_price())
            df_temp['offset'].append(w.get_offset())
            df_temp['upc'].append(w.get_upc())
            df_temp['Shipping Weight'].append(w.get_ship_weight())
            df_temp['wheelimage'].append(w.get_wheel_image())
            bar.update(item_id=all_total)
            all_total += 1

        df = pd.DataFrame(df_temp)

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(r'sheets/save_files/save_file.xlsx', engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer)

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

    def build_wheel_variants_list(self):
        self.wheel_variants_list = []
        for w in self.wheels:
            for v in self.wheels[w].get_variants():
                print(v)
                self.wheel_variants_list.append(self.wheels[w].get_variants()[v])

    # Done
    def add_wheel(self, product_id, wheel_variant):
        if product_id not in self.wheels:
            self.wheels[product_id] = Wheels(wheel_variant)
            self.wheels[product_id].set_product_id(product_id)
        else:
            self.wheels[product_id].add_variant(wheel_variant)
            self.wheels[product_id].set_product_id(product_id)

    # Done
    def delete_wheel(self, product_id):
        del self.wheels[product_id]

    def set_wheel_variants_list(self, wheel_variants_list):
        self.wheel_variants_list = wheel_variants_list

    def get_wheel_variants_list(self):
        return self.wheel_variants_list

    # Done
    def get_wheels(self):
        return self.wheels

    def find_product_id(self, wheel_variant):
        for product_id in self.wheels:
            if wheel_variant.get_style_description() == self.wheels[product_id].get_style_description():
                return product_id
        return None

    def has_variants(self, wheel_variant):
        for product_id in self.wheels:
            if wheel_variant.get_style_description() == self.wheels[product_id].get_style_description():
                return True
        return False
