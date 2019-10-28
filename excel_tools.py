import pandas as pd
import pyprind
from data.Wheels import Wheels
from data.Tires import Tires
from data.WheelVariants import WheelVariants
from data.TireVariants import TireVariants


class ExcelTools:

    @staticmethod
    def find_tire_brand(tire_description):
        tire_dict = {'MOTOCLAW': 'MOTOCLAW',
                     'MOTOBOSS': 'MOTOBOSS',
                     'MOTOFORCE': 'MOTOFORCE',
                     'MOTOHAMMER': 'MOTOHAMMER',
                     'EFX MOTOHAVOK': 'EFX MOTOHAVOK',
                     'MOTOMAX': 'MOTOMAX',
                     'MOTOVATOR': 'MOTOVATOR',
                     'MOTOVATOR R/T': 'MOTOVATOR R/T',
                     'SLINGER': 'SLINGER',
                     'MOTOMTC': 'MOTOMTC'}
        for t in tire_dict:
            if t in tire_description:
                return tire_dict[t]
        return "No Brand"

    @staticmethod
    def read_map_pricing():
        print("Reading Map Pricing")
        df = pd.read_excel(r'sheets/exp_10-21-2019_mapPricing.xlsx')
        total = 1
        all_total = 1
        map_price_dict = {}
        bar = pyprind.ProgBar(len(df.index), monitor=True)
        for i in df.index:
            map_price_dict[str(df['Part Number'][i])] = str(df['Map Price'][i])
            bar.update()
        print("Total Added: ", total)
        print("Total Read: ", all_total)
        return map_price_dict

    @staticmethod
    def read_product_techincal_data_usd_example():
        print("Reading Product Technical Data USD")
        df = pd.read_excel(r'sheets/examples/producttechdatausd_example.xlsx')
        wheels = []
        wheel = None
        total = 1
        all_total = 1
        bar = pyprind.ProgBar(len(df.index), monitor=True)
        for i in df.index:
            if df['MapPrice'][i] != 0:
                wheel = Wheels(str(df['styledescription'][i]),
                               str(df['partnumber'][i]),
                               str(df['partnumberdescription'][i]),
                               str(df['size'][i]),
                               str(df['finish'][i]),
                               str(df['MapPrice'][i]),
                               str(df['offset'][i]),
                               str(int(df['upc'][i])),
                               str(df['Shipping Weight'][i]),
                               str(df['wheelimage'][i]))
            if not wheel is None:
                wheels.append(wheel)
            total += 1
            all_total += 1
            bar.update()
        return wheels

    @staticmethod
    def read_product_technical_data_usd(spread_sheet_name):
        print("Reading Product Technical Data USD")
        df = pd.read_excel(spread_sheet_name)
        wheels = []
        wheel = None
        total = 1
        all_total = 1
        bar = pyprind.ProgBar(len(df.index), monitor=True)
        for i in df.index:
            if df['MapPrice'][i] != 0:
                wheel = WheelVariants(str(df['styledescription'][i]),
                               str(df['partnumber'][i]),
                               str(df['partnumberdescription'][i]),
                               str(df['size'][i]),
                               str(df['finish'][i]),
                               str(df['MapPrice'][i]),
                               str(df['offset'][i]),
                               str(int(df['upc'][i])),
                               str(df['Shipping Weight'][i]),
                               str(df['wheelimage'][i]))
            if not wheel is None:
                wheels.append(wheel)
            total += 1
            all_total += 1
            bar.update()
        return wheels

    @staticmethod
    def read_accessories_data(spread_sheet_name):
        print('Reading Accessory Data')
        df = pd.read_excel(spread_sheet_name)
        accessories = []

        total = 1
        all_total = 1
        bar = pyprind.ProgBar(len(df.index), monitor=True)
        for i in df.index:
            accessory = None

    @staticmethod
    def read_tire_data_usd(spread_sheet_name):
        print('Reading Tire Data USB')
        df = pd.read_excel(spread_sheet_name)
        tires = []

        total = 1
        all_total = 1
        bar = pyprind.ProgBar(len(df.index), monitor=True)
        for i in df.index:
            #print(i)
            tire = None
            if df['MAP'][i] != 0:
                tire = TireVariants(str(df['PartNo'][i]),
                             str(df['TireSize'][i]),
                             str(df['TireDescription'][i]),
                             str(df['TireSizeDescription'][i]),
                             str(int(df['UPC'][i])),
                             str(df['PictureCd'][i]),
                             str(df['Weight'][i]),
                             str(df['MAP'][i]))
            if not tire is None:
                #print(tire)
                tire.set_comparison_var(ExcelTools.find_tire_brand(tire.get_tire_description()))
                tires.append(tire)
            total += 1
            all_total += 1
            bar.update()
        return tires

    @staticmethod
    def compare_tire_data_usd(older_tires, newer_tires, map_only=True):
        # Just need to go through and compare them and make sure
        # nothing needs to be changed on the website

        # This will be basic, just check that map is correct
        upc_to_change = {}
        to_delete = []# list of upcs
        to_add = []
        to_edit = []
        # We need to check for a few things
        # 1) Do any need to be deleted
        for i in older_tires:
            if not i in newer_tires:
                to_delete.append(i)
        upc_to_change['delete'] = to_delete

        # 2) Do any need to be added
        for i in newer_tires:
            if not i in older_tires:
                to_add.append(newer_tires[i])
        upc_to_change['add'] = to_add
        # 3) Do any need to be altered
        for i in newer_tires:
            if i in older_tires:
                if map_only:
                    if newer_tires[i].compare_map_prices(older_tires[i]):
                        to_edit.append({'older': older_tires[i], 'newer': newer_tires[i]})
                else:
                    if newer_tires[i] != older_tires[i]:
                        to_edit.append({'older': older_tires[i], 'newer': newer_tires[i]})
        # Now we have all of the cases where changes need to be made
        # Otherwise, leave everything the same
        return upc_to_change
