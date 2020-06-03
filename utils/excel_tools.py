#!/usr/bin/env python
"""
excel_tools.py: All of the tools needed to read price sheets
"""
import pandas as pd
import pyprind

from utils.wheel_pros_data_feed import get_wheel_update
from utils.wheel_pros_data_feed import get_tire_update

from data.DS18.Products.DS18ProductsVariants import DS18Variants
from data.SAndBFilters.Products.FilterVariants import FilterVariant
from data.WheelPros.Kits.KitVariants import KitVariants
from data.WheelPros.Wheels.WheelVariants import WheelVariants
from data.WheelPros.Tires.TireVariants import TireVariants


class ExcelTools:

    @staticmethod
    def read_generic_product_sheet(spreadshet_name):
        """
        Method that is used to take any product sheet
        and turn the spreadsheet into products
        :param spreadshet_name: Name of the spreadsheet
        :return: array of objects
        """

    @staticmethod
    def read_high_lifter(spreadsheet_name):
        """
        Method that is used to take the HighLifter
        spreadsheet and turn spreadsheet into products
        :param spreadsheet_name: Name of the spreadsheet
        :return: array of objects
        """
        pass

    @staticmethod
    def read_super_atv(spread_sheet_name):
        """
        Method that is used to take the SuperATV
        spreadsheet and turn spreadsheet into products
        :param spread_sheet_name:  Name of the spreadsheet
        :return: array of objects
        """
        pass

    @staticmethod
    def read_ds18(spread_sheet_name):
        """
        Method that is ued to take the DS18
        spreadsheet and turn spreadsheet into products
        :param spread_sheet_name: Name of the spreadsheet
        :return: array of objects
        """

        # TODO: Need to test the method
        # TODO: Make method more more versatile
        print('Reading DS18 Data Sheet')
        df = pd.read_excel(spread_sheet_name, "product_sheets")
        df_needed = pd.read_excel(spread_sheet_name, "for_store")
        ds18_products = []

        # ----------------------------
        ds18_needed = {}
        for i in df_needed.index:
            # Go through and get all of the models we need
            ds18_needed[(str(df_needed['Model'][i]).replace("-", ""))] = str(df_needed['Collection'][i])

        # print(ds18_needed)

        # ----------------------------

        total = 1
        all_total = 1
        bar = pyprind.ProgBar(len(df.index), monitor=True)
        for i in df.index:
            ds18_product = None
            if df['MSRP'][i] != 0 and (df['Model'][i].replace("-", "")) in ds18_needed:
                ds18_product = DS18Variants(str(df['Model'][i]),
                                            str(df['Brand'][i]),
                                            str(df['Name'][i]),
                                            str(df['M/C'][i]),
                                            str(df['MSRP'][i]),
                                            str(df['Dealer'][i]),
                                            str(ds18_needed[df['Model'][i].replace("-", "")]))
            if ds18_product is not None:
                ds18_products.append(ds18_product)
            total += 1
            all_total += 1
            bar.update()
        return ds18_products

    @staticmethod
    def read_s_and_b_filters(spread_sheet_name):
        """
        Method that is used to take the S&B Filters
        spreadsheet and turn spreadsheet into products
        :param spread_sheet_name: Name of the spreadsheet
        :return: array of objects
        """
        print("Reading S&B Filters products")
        df = pd.read_excel(spread_sheet_name)
        products = []
        product = None
        total = 1
        all_total = 1
        bar = pyprind.ProgBar(len(df.index), monitor=True)
        for i in df.index:
            if df["Price"][i] != 0 and df['Type'][i] == 'UTV':
                product = FilterVariant(str(df['S&B Part #'][i]),
                                        str(df['UPC'][i]),
                                        str(df['Product Description'][i]),
                                        str(df['Product Description / Fitment'][i]),
                                        str(df['Type'][i]),
                                        str(df['Price'][i]),
                                        "image_url")
            if product is not None:
                products.append(product)
            total += 1
            all_total += 1
            bar.update()
        return products

    @staticmethod
    def find_tire_brand(tire_description):
        """
        Method used to pull tags out of title
        :param tire_description:
        :return: returns the tag for the brand
        """
        # TODO: Need to test the method
        # TODO: Make method more more versatile
        # TODO: Need to make more methods to find tags

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
    def read_map_pricing(spread_sheet_name):
        """
        Read in the map pricing
        :param spread_sheet_name: name of the sheet
        :return: returns map price dictionary
        """
        # TODO: Need to test the method
        # TODO: Make method more more versatile

        print("Reading Map Pricing")
        df = pd.read_excel(spread_sheet_name)
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
    def check_wheel_brand(param):
        brands = ["FUEL UTV",
                  "MSA OFFROAD WHEELS",
                  "XD ATV"]

        if param in brands:
            return True
        else:
            return False

    @staticmethod
    def read_product_technical_data_usd(spread_sheet_name):
        """
        Read in Wheel Proos - Read Product Technical Data USD
        :param spread_sheet_name: name of the sheet
        :return: List of Tire objects
        """
        # TODO: Need to test the method
        # TODO: Make method more more versatile

        print("Reading Product Technical Data USD")
        # Read Spreadsheet from wheel pros dealerline
        df = pd.read_excel(spread_sheet_name)
        wheels = []
        # Date Feed
        # Read Data Feed
        wheel_feed = get_wheel_update()
        total = 1
        all_total = 1
        bar = pyprind.ProgBar(len(wheel_feed), monitor=True)
        for i in df.index:
            try:
                wheel = None
                if df['W.D. USD'][i] != 0 and ExcelTools.check_wheel_brand(str(df['WhlManufactNm'][i])) and\
                        int(wheel_feed[str(df['partnumber'][i])].inventory_quantity) != 0:
                    upc_temp = ""
                    if str(df['upc'][i]) != "nan":
                        upc_temp = str(int(df['upc'][i]))
                    wheel = WheelVariants(wheel_feed[df['partnumber'][i]],
                                          int(wheel_feed[str(df['partnumber'][i])].inventory_quantity),
                                          str(df['styledescription'][i]),
                                          str(df['partnumber'][i]),
                                          str(df['partnumberdescription'][i]),
                                          str(df['size'][i]),
                                          str(df['finish'][i]),
                                          str(wheel_feed[str(df['partnumber'][i])].price),
                                          str(wheel_feed[str(df['partnumber'][i])].price),
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
                                          upc_temp,
                                          str(df['InvOrderType'][i]),
                                          str(df['RearOnly'][i]),
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
                                          str(df['BoltPatternMm2'][i]),
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
                                          str(wheel_feed[str(df['partnumber'][i])].image_url),
                                          str(df['Prop65 Chemical 1'][i]),
                                          str(df['Prop65 Chemical 2'][i]),
                                          str(df['Prop65 Chemical 3'][i]))

                if wheel is not None:
                    wheels.append(wheel)
            except KeyError:
                print(df["partnumber"][i],"not found!")
                pass
            total += 1
            all_total += 1
            bar.update()
        return wheels



    @staticmethod
    def compare_product_technical_data_usd(old_sheet_name, new_sheet_name):
        old_wheels = ExcelTools.read_product_technical_data_usd(old_sheet_name)
        new_wheels = ExcelTools.read_product_technical_data_usd(new_sheet_name)

        upc_to_add = []
        upc_to_delete = []
        upc_to_edit = []

        df_temp = {'upc': [],
                   'action': [],
                   'name': []}

        # There are three different scenerios of what could happen
        # 1) New Wheel to add
        for n in new_wheels:
            found_wheel = False
            for o in old_wheels:
                if n.get_upc() == o.get_upc():
                    found_wheel = True
            if not found_wheel:
                # TODO: 1) Wheel Needs to be added
                df_temp['upc'].append(n.get_upc())
                df_temp['action'].append("Add")
                df_temp['name'].append(n.get_style_description())

        # 2) Delete Wheel
        for o in old_wheels:
            found_wheel = False
            for n in new_wheels:
                if o.get_upc() == n.get_upc():
                    found_wheel = True
            if not found_wheel:
                # TODO: 2) Wheel Needs to be deleted
                df_temp['upc'].append(o.get_upc())
                df_temp['action'].append("Remove")
                df_temp['name'].append(n.get_style_description())

        # 3) Need to edit the wheel
        for o in old_wheels:
            for n in new_wheels:
                if o.get_upc() == n.get_upc():
                    # We have 2 wheels, and need to check
                    # if edits need to be made
                    if o == n:
                        # TODO: 3) Wheel Needs to be editted
                        df_temp['upc'].append(o.get_upc())
                        df_temp['action'].append("Edit")
                        df_temp['name'].append(n.get_style_description())

        df = pd.DataFrame(df_temp)

        # Create a Pandas Excel writer using XlsxWriter as the engine.
        writer = pd.ExcelWriter(r'sheets/save_files/wheel_changes.xlsx', engine='xlsxwriter')

        # Convert the dataframe to an XlsxWriter Excel object.
        df.to_excel(writer)

        # Close the Pandas Excel writer and output the Excel file.
        writer.save()

    @staticmethod
    def read_tire_data_usd(spread_sheet_name):
        """
        Reads in tire data and returns Tire objects
        :param spread_sheet_name: name of the sheet to read in
        :return: Tire objects
        """
        # TODO: Need to test the method
        # TODO: Make method more more versatile
        print('Reading Tire Data USB')
        df = pd.read_excel(spread_sheet_name)
        tires = []

        excluded_tires = ["WILDPEAK A/T3W",
                          "TRAIL GRAPPLER",
                          "TERRA GRAPPLER G2",
                          "RIDGE GRAPPLER"]

        # Date Feed
        tire_feed = get_tire_update()

        total = 1
        all_total = 1
        bar = pyprind.ProgBar(len(df.index), monitor=True)
        for i in df.index:
            try:
                tire = None
                if df['PowerSports'][i] != 0 and df['FullModelName'][i] not in excluded_tires and int(tire_feed[str(df['PartNo'][i])].total_qqh) != 0:
                    tire = TireVariants(int(tire_feed[str(df['PartNo'][i])].total_qqh),
                                          str(df['TireMfrCd'][i]),
                                          str(df['PartNo'][i]),
                                          str(df['TireSize'][i]),
                                          str(df['TireDescription'][i]),
                                          str(df['TireSizeDescription'][i]),
                                          str(df['LoadIndex'][i]),
                                          str(df['PSI'][i]),
                                          str(df['SpeedRating'][i]),
                                          str(tire_feed[str(df['PartNo'][i])].usd),
                                          str(df['StgItemCd'][i]),
                                          str(df['eMarked'][i]),
                                          str(df['UPC'][i]),
                                          str(df['SectionWidth'][i]),
                                          str(df['Series'][i]),
                                          str(df['RimDiameter'][i]),
                                          str(df['TireDiameter'][i]),
                                          str(tire_feed[str(df['PartNo'][i])].image_url),
                                          str(df['Weight'][i]),
                                          str(df['TireDiameter2'][i]),
                                        str(df['MinWidthIn'][i]),
                                        str(df['MaxWidthIn'][i]),
                                        str(df['MaxLoad'][i]),
                                        str(df['PowerSports'][i]),
                                        str(tire_feed[str(df['PartNo'][i])].us_map),
                                        str(df['Sts'][i]),
                                        str(df['FullModelName'][i]),
                                        str(df['TreadDepth'][i]),
                                        str(df['Ply'][i]),
                                        str(df['ConstructionType'][i]),
                                        str(df['Terrain'][i]),
                                        str(df['MaxLoadDual'][i]),
                                        str(df['MaxPressure'][i]),
                                        str(df['ApprovedRimWidth'][i]),
                                        str(df['UTQG'][i]),
                                        str(df['Treadwear'][i]),
                                        str(df['Traction'][i]),
                                        str(df['Temperature'][i]),
                                        str(df['SourceCountry'][i]),
                                        str(df['MileageWarranty'][i]))
                    if tire is not None:
                        tires.append(tire)
            except KeyError:
                print(df["PartNo"][i], "not found!")
            total += 1
            all_total += 1
            bar.update()
        return tires

    @staticmethod
    def compare_tire_data(old_sheet_name, new_sheet_name):
        pass
    @staticmethod
    def read_kit_data(spread_sheet_name):
        print("Reading Kit Data")
        df = pd.read_excel(spread_sheet_name)
        kits = []
        kit = None
        total = 1
        all_total = 1
        bar = pyprind.ProgBar(len(df.index), monitor=True)
        for i in df.index:
            kit = KitVariants(str(df['upc'][i]),
                              str(df['Name'][i]),
                              str(df['Wheel'][i]),
                              str(df['Tire'][i]),
                              str(df['MSRP'][i]),
                              str(df['Size'][i]))
            #print(str(df['upc'][i]))
            #print(kit.get_upc())
            if kit is not None:
                kits.append(kit)
            total += 1
            all_total += 1
            bar.update()
        return kits

    @staticmethod
    def compare_kit_data(old_sheet_name, new_sheet_name):
        pass
    @staticmethod
    def compare_tire_data_usd(older_tires, newer_tires, map_only=True):
        """
        This method is mean't to compare 2 sets of Tire objects, and edits the existing tires to combine the
        older_tires and newer_tires
        :param older_tires: Tires before addition
        :param newer_tires: Tires after
        addition
        :param map_only: If you only want to change the map price
        :return: Returns upc, which is a
        dictionary with everything that needs to happen {{'delete'}:[], {'add'}:[], {'edit'}:[]}
        """
        # TODO: Need to edit this method and start using it, it is currently only map_price

        print("Compare Tire Data USD")
        print("Map Price Only: ", map_only)
        # Just need to go through and compare them and make sure
        # nothing needs to be changed on the website

        # This will be basic, just check that map is correct
        # upcs that needs to be changed
        upc_to_change = {}
        # Tires to delete
        to_delete = []
        # Tires to add
        to_add = []
        # Tires to edit
        to_edit = []
        # We need to check for a few things
        # --------------------------------------
        # 1) Do any need to be deleted
        for i in older_tires:
            # if the new tire does not exist yet
            if i not in newer_tires:
                # delete it from older tires
                to_delete.append(i)
        # mark the tire to delete
        upc_to_change['delete'] = to_delete
        # --------------------------------------
        # 2) Do any need to be added
        for i in newer_tires:
            # if the new tire wasn't there before
            if i not in older_tires:
                # add it into the tires
                to_add.append(newer_tires[i])
        # mark the tire to add
        upc_to_change['add'] = to_add
        # --------------------------------------
        # 3) Do any need to be altered
        # Go through Newer tires
        for i in newer_tires:
            # Go through Older tires
            if i in older_tires:
                # Check if we only want to change the map price
                if map_only:
                    # Compare the prices, and see if they need to be changed
                    if newer_tires[i].compare_map_prices(older_tires[i]):
                        # Mark it to edit
                        to_edit.append({'older': older_tires[i], 'newer': newer_tires[i]})
                else:
                    # Compare the entire product to see if anything needs to be changed
                    if newer_tires[i] != older_tires[i]:
                        # Mark it to edit
                        to_edit.append({'older': older_tires[i], 'newer': newer_tires[i]})
        # Now we have all of the cases where changes need to be made
        # Otherwise, leave everything the same
        return upc_to_change

#ExcelTools.compare_product_technical_data_usd("exp_11-28-2019-producttechdatausd.xlsx","exp_12-11-2019-producttechdatausd.xlsx")