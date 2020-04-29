from ftplib import FTP
import pandas as pd
import logging

class InventoryFeedWheel:
    def __init__(self, part_number, total_qqh, image_src, map_price, msrp_price):
        self.part_number = part_number
        self.total_qqh = total_qqh
        self.image_src = image_src
        self.map_price = map_price
        self.msrp_price = msrp_price

    def __str__(self):
        s = ""
        s += "Part Num: %s"% str(self.part_number)
        s += "Total QQH: %s"% str(self.total_qqh)
        s += "Image src: %s"% str(self.image_src)
        s += "Map Price: %s"% str(self.map_price)
        s += "MSRP Price: %s"% str(self.msrp_price)
        return s

class InventoryFeedTire:
    def __init__(self, brand, part_number, description, image_url, inv_order_type, total_qqh, usd, us_map, run_date):
        self.brand = brand
        self.part_number = part_number
        self.description = description
        self.image_url = image_url
        self.inv_order_type = inv_order_type
        self.total_qqh = total_qqh
        self.usd = usd
        self.us_map = us_map
        self.run_date = run_date
    def __str__(self):
        s = ""
        s += "Brand: %s"% str(self.brand)
        s += "Part Num: %s"% str(self.part_number)
        s += "Total QQH: %s"% str(self.total_qqh)
        return s

def ftp_method(file_name):
    """
    This method refreshes all files from the ftp for Wheel Pros
    :param: file_name: TireInvPriceDataUS.csv, WheelInvPriceDataUS.csv
    :return:
    """
    logging.debug("Starting ftp method")
    ftp = FTP("ftp.wheelpros.com")
    ftp.login("ftp.wheelpros.com|1091543", "J5PU886qN2Qmhp5U")

    ftp.cwd("WheelPros\\US")
    ftp.retrlines('LIST')

    with open(f'{file_name}', 'wb') as fp:
        ftp.retrbinary(f'RETR {file_name}', fp.write)
    ftp.quit()
    logging.debug("Ending ftp method")

def get_tire_update():
    logging.debug("Starting Tire Update")
    df = pd.read_csv('TireInvPriceDataUS.csv', encoding="ISO-8859-1", usecols=['Brand', 'PartNumber', 'Description', 'ImageURL', 'InvOrderType', 'TotalQOH', 'USD', 'USMAP', 'RunDate'])
    result = df.to_dict(orient='records')

    tire_update = {}
    for row in result:
        inv_feed_tire = InventoryFeedTire(row['Brand'], row['PartNumber'], row['Description'], row['ImageURL'], row['InvOrderType'], row['TotalQOH'], row['USD'], row['USMAP'], row['RunDate'])
        tire_update.update({str(inv_feed_tire.part_number):inv_feed_tire})
    logging.debug("Ending Tire Update")
    return tire_update

def get_wheel_update():
    logging.debug("Starting Wheel Update")
    df = pd.read_csv(f'WheelInvPriceDataUS.csv', usecols=['PartNumber', 'TotalQOH', 'ImageURL', 'USMAP', 'USD'])
    result = df.to_dict(orient='records')

    wheel_update = {}
    for row in result:
        inv_feed_wheel = InventoryFeedWheel(row['PartNumber'], row['TotalQOH'], row['ImageURL'], row['USMAP'], row['USD'])
        wheel_update.update({str(inv_feed_wheel.part_number):inv_feed_wheel})
    logging.debug("Ending Wheel Update")
    return wheel_update

get_tire_update()