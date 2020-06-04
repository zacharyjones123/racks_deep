from ftplib import FTP
import pandas as pd
import logging

from data.shopify_product import ShopifyProductVariant


def ftp_method(file_name):
    """
    This method refreshes all files from the ftp for Wheel Pros
    :param: file_name: TireInvPriceDataUS.csv, WheelInvPriceDataUS.csv
    :return:
    """
    logging.debug("Starting ftp method")
    ftp = FTP(host="ftp.wheelpros.com")
    ftp.set_pasv(True)
    # J5PU886qN2Qmhp5U
    ftp.login("ftp.wheelpros.com|1091543", "J5PU886qN2Qmhp5U")

    ftp.cwd("WheelPros/US")
    ftp.retrlines('LIST')

    with open(f'{file_name}', 'wb') as fp:
        ftp.retrbinary(f'RETR {file_name}', fp.write)
    ftp.quit()
    logging.debug("Ending ftp method")


def get_tire_update():
    logging.debug("Starting Tire Update")
    df = pd.read_csv('sheets/WheelPros/TireInvPriceDataUS.csv', encoding="ISO-8859-1",
                     usecols=['Brand', 'PartNumber', 'Description', 'ImageURL', 'TotalQOH', 'USD',
                              'USMAP'])
    result = df.to_dict(orient='records')

    tire_update = {}
    for row in result:
        inv_feed_tire = ShopifyProductVariant(row["USMAP"] if row["USMAP"] == 0 else row["USD"],
                                              row['Brand'],
                                               'no',
                                               'no',
                                              row['PartNumber'],
                                               row['TotalQOH'],
                                               0,
                                               row['ImageURL'],
                                               )
        tire_update.update({str(inv_feed_tire.sku): inv_feed_tire})
    logging.debug("Ending Tire Update")
    return tire_update


def get_wheel_update():
    logging.debug("Starting Wheel Update")
    df = pd.read_csv(f'sheets/WheelPros/WheelInvPriceDataUS.csv',
                     usecols=['USD', 'USMAP', "Size", "BoltPattern", "Offset", "PartNumber", "TotalQOH",
                              "ShippingWeight", "ImageURL"])
    result = df.to_dict(orient='records')

    wheel_update = {}
    for row in result:
        inv_feed_wheel = ShopifyProductVariant(row["USMAP"] if row['USMAP'] == 0 else row["USD"],
                                               row['Size'],
                                               row['BoltPattern'],
                                               row['Offset'],
                                               row['PartNumber'],
                                               row['TotalQOH'],
                                               row['ShippingWeight'],
                                               row['ImageURL'])
        wheel_update.update({str(inv_feed_wheel.sku): inv_feed_wheel})
    logging.debug("Ending Wheel Update")
    return wheel_update