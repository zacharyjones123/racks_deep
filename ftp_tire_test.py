from ftplib import FTP
import csv

class InventoryFeedTire:
    def __init__(self, brand, part_number, description, image_url, inv_order_type, total_qqh, usd, us_map, run_date, division):
        self.brand = brand
        self.part_number = part_number
        self.description = description
        self.image_url = image_url
        self.inv_order_type = inv_order_type
        self.total_qqh = total_qqh
        self.usd = usd
        self.us_map = us_map
        self.run_date = run_date
        self.division = division
    def __str__(self):
        s = ""
        s += "Brand: %s"% str(self.brand)
        s += "Part Num: %s"% str(self.part_number)
        s += "Total QQH: %s"% str(self.total_qqh)
        return s

def get_tire_update():
    ftp = FTP("ftp.wheelpros.com")
    ftp.login("ftp.wheelpros.com|1091543", "J5PU886qN2Qmhp5U")

    ftp.cwd("WheelPros\\US")
    ftp.retrlines('LIST')

    with open('TireInvPriceDataUS.csv', 'wb') as fp:
        ftp.retrbinary('RETR TireInvPriceDataUS.csv', fp.write)
    ftp.quit()

    input_file = csv.DictReader(open("TireInvPriceDataUS.csv"))
    total_lines = 0

    tire_update = {}
    for row in input_file:
        items = list(row.items())
        print(items)
        total_lines += 1
        inv_feed_tire = InventoryFeedTire(items[0][1], items[1][1], items[2][1], items[3][1], items[4][1], items[70][1], items[71][1], items[72][1], items[73][1], items[74][1])
        tire_update.update({str(inv_feed_tire.part_number):inv_feed_tire})
    return tire_update

#get_tire_update()