from ftplib import FTP
import pandas as pd
import csv

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


def get_wheel_update():
    """
    This method refreshes all files from the ftp for Wheel Pros
    :return:
    """
    ftp = FTP("ftp.wheelpros.com")
    ftp.login("ftp.wheelpros.com|1091543", "J5PU886qN2Qmhp5U")

    ftp.cwd("WheelPros\\US")
    ftp.retrlines('LIST')

    with open('WheelInvPriceDataUS.csv', 'wb') as fp:
        ftp.retrbinary('RETR WheelInvPriceDataUS.csv', fp.write)
    ftp.quit()

    input_file = csv.DictReader(open("WheelInvPriceDataUS.csv"))
    total_lines = 0

    wheel_update = {}
    for row in input_file:
        items = list(row.items())
        total_lines += 1
        #print(items)
        inv_feed_wheel = InventoryFeedWheel(items[0][1], items[81][1], items[12][1], items[83][1], items[82][1])
        wheel_update.update({str(inv_feed_wheel.part_number):inv_feed_wheel})
    return wheel_update

#get_wheel_update()