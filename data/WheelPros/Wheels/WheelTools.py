from xlrd import XLRDError

from data.WheelPros.Wheels.WheelVariants import WheelVariants
from data.WheelPros.Wheels.Wheels import Wheels
import pandas as pd
import pyprind


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
        try:
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
                                      str(df['W.D. USD']),
                                      str(df['MapPrice'][i]),
                                      str(df['diameter'][i]),
                                      str(df['width'][i]),
                                      str(df['lugcount'][i]),
                                      str(df['Bolt Pattern Metric'][i]),
                                      str(df['Bolt Pattern US'][i]),
                                      str(df['offset'][i]),
                                      str(df['backspacing'][i]),
                                      str(df['centerbore'][i]),
                                      str(df['Load Rating Lbs'][i]),
                                      str(df['Load Rating Kgs'][i]),
                                      str(df['Hub Ring Included'][i]),
                                      str(df['upc'][i]),
                                      str(df['InvOrderType'][i]),
                                      str(df['RearOnly']),
                                      str(df['HubClearance'][i]),
                                      str(df['BarrelConfig'][i]),
                                      str(df['CapPartNo'][i]),
                                      str(df['CapHardware'][i]),
                                      str(df['QtyOfCapScrews'][i]),
                                      str(df['Cap Wrench'][i]),
                                      str(df['Testing'][i]),
                                      str(df['PictureCd']),
                                      str(df['MaxOffset'][i]),
                                      str(df['MinOffset'][i]),
                                      str(df['Cap Style'][i]),
                                      str(df['OtherAccessories'][i]),
                                      str(df['TPMS Compatable'][i]),
                                      str(df['Wheel Weight'][i]),
                                      str(df['Shipping Weight'][i]),
                                      str(df['WhlManufactCd'][i]),
                                      str(df['WhlManufactNm'][i]),
                                      str(df['DisplayModelNo']),
                                      str(df['SortGroup'][i]),
                                      str(df['WhlModelNm'][i]),
                                      str(df['Full ModelName'][i]),
                                      str(df['Country of Origin'][i]),
                                      str(df['WidthIn'][i]),
                                      str(df['AbrvFinishDesc'][i]),
                                      str(df['Box Label Description'][i]),
                                      str(df['Finish Warranty'][i]),
                                      str(df['BoltPatternMm1'][i]),
                                      str(df['BoltPatternMm2']),
                                      str(df['SmallestBoltPatternMm'][i]),
                                      str(df['LargestBoltPatternMm'][i]),
                                      str(df['MinLugCnt'][i]),
                                      str(df['MaxLugCnt'][i]),
                                      str(df['OpenEndCap'][i]),
                                      str(df['RivetPartNo'][i]),
                                      str(df['RivetQty'][i]),
                                      str(df['PVDFinish'][i]),
                                      str(df['StainlessLip'][i]),
                                      str(df['FlowFormed'][i]),
                                      str(df['Forged'][i]),
                                      str(df['TwoPiece'][i]),
                                      str(df['SteelWheel'][i]),
                                      str(df['TrueBeadLock'][i]),
                                      str(df['OffRoadUseOnly'][i]),
                                      str(df['Patent'][i]),
                                      str(df['Lip Depth'][i]),
                                      str(df['Construction'][i]),
                                      str(df['Material'][i]),
                                      str(df['FancyFinishDesc'][i]),
                                      str(df['wheelimage'][i]),
                                      str(df['Prop65 Chemical 1'][i]),
                                      str(df['Prop65 Chemical 2'][i]),
                                      str(df['Prop65 Chemical 3'][i]))
                wheel_variants_list.append(wheel_variant)
                bar.update(item_id=all_total)
                all_total += 1
            self.wheel_variants_list = wheel_variants_list
            # self.build_wheels()
        except XLRDError:
            print("Save file is empty or does not exist, try again")
        except FileNotFoundError:
            print("File does not exist")

    def save_wheel_variants_to_file(self):
        print("Saving Save File")
        # TODO: Need to fix this
        # self.build_wheel_variants_list()
        bar = pyprind.ProgBar(len(self.wheel_variants_list), monitor=True)
        all_total = 1
        df_temp = {'styledescription' : [],
                   'partnumber' : [],
                   'partnumberdescription' : [],
                    'size' : [],
                    'finish' : [],
                     'W.D. USD' : [],
                    'MapPrice' : [],
                    'diameter' : [],
                    'width' : [],
                    'lugcount' : [],
                    'Bolt Pattern Metric' : [],
                    'Bolt Pattern US' : [],
                    'offset' : [],
                     'backspacing' : [],
                     'centerbore' : [],
                      'Load Rating Lbs' : [],
                      'Load Rating Kgs' : [],
                      'Hub Ring Included' : [],
                      'upc' : [],
                      'InvOrderType' : [],
                      'RearOnly' : [],
                       'HubClearance' : [],
                       'BarrelConfig' : [],
                      'CapPartNo' : [],
                     'CapHardware' : [],
                   'QtyOfCapScrews' : [],
                   'Cap Wrench' : [],
                   'Testing' : [],
                   'PictureCd' : [],
                    'MaxOffset' : [],
                   'MinOffset' : [],
                     'Cap Style' : [],
                     'OtherAccessories' : [],
                       'TPMS Compatable' : [],
                      'Wheel Weight' : [],
                      'Shipping Weight' : [],
                      'WhlManufactCd' : [],
                      'WhlManufactNm' : [],
                     'DisplayModelNo' : [],
                    'SortGroup' : [],
                    'WhlModelNm' : [],
                   'Full ModelName' : [],
                   'Country of Origin' : [],
                    'WidthIn' : [],
                     'AbrvFinishDesc' : [],
                     'Box Label Description' : [],
                      'Finish Warranty' : [],
                      'BoltPatternMm1' : [],
                       'BoltPatternMm2' : [],
                      'SmallestBoltPatternMm' : [],
                       'LargestBoltPatternMm' : [],
                      'MinLugCnt' : [],
                        'MaxLugCnt' : [],
                         'OpenEndCap' : [],
                         'RivetPartNo' : [],
                        'RivetQty' : [],
                        'PVDFinish' : [],
                       'StainlessLip' : [],
                      'FlowFormed' : [],
                      'Forged' : [],
                       'TwoPiece' : [],
                       'SteelWheel' : [],
                      'TrueBeadLock' : [],
                     'OffRoadUseOnly' : [],
                      'Patent' : [],
                      'Lip Depth' : [],
                      'Construction' : [],
                     'Material' : [],
                       'FancyFinishDesc' : [],
                       'wheelimage' : [],
                      'Prop65 Chemical 1' : [],
                      'Prop65 Chemical 2' : [],
                      'Prop65 Chemical 3' : [],
                   }

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
            df_temp['Bolt Pattern Metric'].append(w.get_bolt_pattern_metric())
            df_temp['Bolt Pattern US'].append(w.get_bolt_pattern_us())
            df_temp['W.D. USD'].append(w.get_msrp_price())
            df_temp['lugcount'].append(w.get_lug_count())
            df_temp['Bolt Pattern Mm1'].append(w.get_bolt_pattern_mm1())
            df_temp['Bolt Pattern Mm2'].append(w.get_bolt_pattern_mm2())
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
        # Save a copy of the wheel
        wheel_copy = self.wheels[product_id]
        del self.wheels[product_id]

        # Also need to delete wheel_variants also
        new_wheel_variants_list = []
        for w in self.wheel_variants_list:
            if w.get_style_description() == wheel_copy.get_style_description():
                new_wheel_variants_list.append(w)
        self.wheel_variants_list = new_wheel_variants_list

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
