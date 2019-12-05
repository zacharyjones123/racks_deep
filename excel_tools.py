#!/usr/bin/env python
"""
excel_tools.py: All of the tools needed to read price sheets
"""
import pandas as pd
import pyprind

from data.SAndBFilters.Products.Filter import Filter
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
            if df["Price Type - Retail/ MAP"][i] != 0:
                product = Filter(str(df['S&B Part #'][i]),
                                      str(df['UPC'][i]),
                                      str(df['Product Description'][i]),
                                      str(df['Product Description / Fitment'][i]),
                                      str(df['Type'][i]),
                                      str(df['Price Type - Retail / MAP'][i]))
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
    def read_product_technical_data_usd(spread_sheet_name):
        """
        Read in Wheel Proos - Read Product Technical Data USD
        :param spread_sheet_name: name of the sheet
        :return: List of Tire objects
        """
        # TODO: Need to test the method
        # TODO: Make method more more versatile

        print("Reading Product Technical Data USD")
        df = pd.read_excel(spread_sheet_name)
        wheels = []
        wheel = None
        total = 1
        all_total = 1
        bar = pyprind.ProgBar(len(df.index), monitor=True)
        for i in df.index:
            if df['W.D. USD'][i] != 0:
                upc_temp = ""
                if str(df['upc'][i]) != "nan":
                    upc_temp = str(int(df['upc'][i]))
                wheel = WheelVariants(str(df['styledescription'][i]),
                                      str(df['partnumber'][i]),
                                      str(df['partnumberdescription'][i]),
                                      str(df['size'][i]),
                                      str(df['finish'][i]),
                                      str(df['MapPrice'][i]),
                                      str(df['offset'][i]),
                                      upc_temp,
                                      str(df['Shipping Weight'][i]),
                                      str(df['wheelimage'][i]),
                                      str(df['Bolt Pattern Metric'][i]),
                                      str(df['Bolt Pattern US'][i]),
                                      str(df['W.D. USD'][i]),
                                      str(df['lugcount'][i]),
                                      str(df['BoltPatternMm1'][i]),
                                      str(df['BoltPatternMm2'][i]))
            if wheel is not None:
                wheels.append(wheel)
            total += 1
            all_total += 1
            bar.update()
        return wheels



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

        total = 1
        all_total = 1
        bar = pyprind.ProgBar(len(df.index), monitor=True)
        for i in df.index:
            tire = None
            if df['PowerSports'][i] != 0:
                tire = TireVariants(str(df['TireMfrCd'][i]),
                                      str(df['PartNo'][i]),
                                      str(df['TireSize'][i]),
                                      str(df['TireDescription'][i]),
                                      str(df['TireSizeDescription'][i]),
                                      str(df['LoadIndex'][i]),
                                      str(df['PSI'][i]),
                                      str(df['SpeedRating'][i]),
                                      str(df['Wd'][i]),
                                      str(df['StgItemCd'][i]),
                                      str(df['eMarked'][i]),
                                      str(df['UPC'][i]),
                                      str(df['SectionWidth'][i]),
                                      str(df['Series'][i]),
                                      str(df['RimDiameter'][i]),
                                      str(df['TireDiameter'][i]),
                                      str(df['PictureCd'][i]),
                                      str(df['Weight'][i]),
                                      str(df['TireDiameter2'][i]),
                                    str(df['MinWidthIn'][i]),
                                    str(df['MaxWidthIn'][i]),
                                    str(df['MaxLoad'][i]),
                                    str(df['PowerSports'][i]),
                                    str(df['MAP'][i]),
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
            total += 1
            all_total += 1
            bar.update()
        return tires

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
                              str(df['Price'][i]))
            if kit is not None:
                kits.append(kit)
            total += 1
            all_total += 1
            bar.update()
        return kits

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
