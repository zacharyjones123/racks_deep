"""
control_center.py: Where everything from the project will
be ran
"""

import progressbar
import time
from tqdm import tqdm
# from shopify_tools import ShopifyTools

# TODO: Need to add more wrappers
from excel_tools import ExcelTools
from shopify_tools import ShopifyTools
from shopify_tools_wheels import ShopifyToolsWheels



def update_wheel_pros_wheels(spreadsheet_name):
    """
    Update Wheel Pros Wheels
    :param spreadsheet_name: Name of the spreadsheet
    :return: report of what was updated
    """
    pass


def update_wheel_pros_tires(spreadsheet_name):
    """
    Update Wheel Pros Tires
    :param spreadsheet_name: Name of the spreadsheet
    :return: report of what was updated
    """
    pass


def update_wheel_pros_kits(spreadsheet_name):
    """
    Update Wheel Pros Kits
    :param spreadsheet_name: Name of the spreadsheet
    :return:  report of what was reported
    """
    pass


def update_super_atv_wheels(spreadsheet_name):
    """
    Update SuperATV Wheels
    :param spreadsheet_name: Name of the spreadsheet
    :return:  report of what was reported
    """
    pass


def update_high_lifter_wheels(spreadsheet_name):
    """
    Update High Lifter Wheels
    :param spreadsheet_name: Name of the spreadsheet
    :return: report of what was reported
    """
    pass


def update_s_and_b_filters(spreadsheet_name):
    """
    Update S&B Filters Filters
    :param spreadsheet_name: Name of the spreadsheet
    :return: report of what was reported
    """
    pass


def delete_all_wheel_pros_wheels():
    """
    Function wrapper over the ShopifyAPI
    :return: Nothing
    """
    # Call to ShopifyTools
    #ShopifyTools.delete_all_wheels()


def menu():
    print("Control Center Started!")
    print("-----------------------------------------")
    print("Loading Information From Local System")
    print("Loading Information From Shopify")
    print("Complete!")
    print("What would you like to do today?")
    print("1) Update Spreadsheets")
    print("What distributor would you like to update?")
    print("   a) Wheel Pros")
    print("      - Wheels")
    print("      - Tires")
    print("      - Kits")
    print("   b) SuperATV ")
    print("      - Wheels ")
    print("   c) HighLifter")
    print("      - Wheels")
    print("   d) S & B Filters")
    print("      - Filters")


def welcome_message():
    """
    Print out welcome message
    :return: Nothing
    """
    print("Welcome To Racks Deep Support")
    print("What needs to be completed today?")
    print("1) Add New Products")
    print("2) Update Products")
    print("3) Delete Products")
    print("4) Update Local Data from Shopify Database")
    print("5) See Finances")
    print("Choice: ")
    option = input()
    if option == "1":
        menu_add_new_products()


def menu_add_new_products():
    print("----------------------------")
    print("Adding New Products")
    print("----------------------------")
    print("Which Distributor?")
    print("1) Wheel Pros")
    print("2) SuperATV")
    print("3) HighLifter")
    print("4) S&B Filters")
    option = input()
    if option == "1":
        menu_add_new_products_wheel_pros()
    elif option == "2":
        menu_add_new_products_super_atv()
    elif option == "3":
        menu_add_new_products_highlifter()
    elif option == "4":
        menu_add_new_products_s_and_b_filters()
    else:
        print("Not an option, sorry")


def menu_update_products():
    print("----------------------------")
    print("Updating Products")
    print("----------------------------")
    print("Which Distributor?")
    print("1) Wheel Pros")
    print("2) SuperATV")
    print("3) HighLifter")
    print("4) S&B Filters")
    option = input()
    if option == "1":
        pass


def menu_delete_products():
    print("----------------------------")
    print("Deleting products")
    print("----------------------------")
    print("Which Distributor?")
    print("1) Wheel Pros")
    print("2) SuperATV")
    print("3) HighLifter")
    print("4) S&B Filters")
    option = input()
    if option == "1":
        pass


def menu_add_new_products_wheel_pros():
    print("----------------------------")
    print("Adding New Wheel Pros Products")
    print("----------------------------")
    print("Spreadsheet Name: ")
    spreadsheet_name = input()
    # TODO: Add in the method that will complete this


def menu_add_new_products_super_atv():
    print("----------------------------")
    print("Adding New SuperATV Products")
    print("----------------------------")
    print("Spreadsheet Name: ")
    spreadsheet_name = input()
    # TODO: Add in the method that will complete this


def menu_add_new_products_highlifter():
    print("----------------------------")
    print("Adding New HighLifter Products")
    print("----------------------------")
    print("Spreadsheet Name: ")
    spreadsheet_name = input()
    # TODO: Add in the method that will complete this


def menu_add_new_products_s_and_b_filters():
    print("----------------------------")
    print("Adding New S&B Filters Products")
    print("----------------------------")
    print("Spreadsheet Name: ")
    spreadsheet_name = input()
    # TODO: Add in the method that will complete this


if __name__ == '__main__':
    welcome_message()
