"""
control_center.py: Where everything from the project will
be ran
"""

import progressbar
import time
from tqdm import tqdm
from shopify_tools import ShopifyTools

#TODO: Need to add more wrappers

def delete_all_wheel_pros_wheels():
    """
    Function wrapper over the ShopifyAPI
    :return: Nothing
    """
    # Call to ShopifyTools
    ShopifyTools.delete_all_wheels()


if __name__ == '__main__':
    #ShopifyTools.delete_all_wheels()
    print("Control Center Started!")
    print("-----------------------------------------")
    print("Loading Information From Local System")
    print("Loading Information From Shopify")
    print("Complete!")
    print("What would you like to do today?")
    print("1) Update Spreadsheets")
    print("   a) Wheel Pros")
    print("      - Wheels")
    print("      - Tires")
    print("      - Kits")
    print("Updating Wheels")