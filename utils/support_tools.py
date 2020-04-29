"""
The purpose of this file is to give support a way of seeing
data quickly and without having to look at papers

This will include tools such as:
- Looking up if a product exists
- Looking up what the product costs
- Looking up if a product is in stock

The format will be that each tool gets it's own method and then
I will go back and figure out how to make it more user friendly
"""


class SupportToolKit:
    @staticmethod
    def lookup_price_for_product(product_id):
        """
        Method will take the product_id, and
        return what the price is on shopify
        :param product_id: shopify id for the product
        :return: the price of the product
        """
        pass

    @staticmethod
    def change_price_for_product(product_id, new_price):
        """
        Method will take the product_id and
        change the price to what it needs to be now.

        This is when we want to change our margins
        quickly
        :param product_id:  shopify id for the product
        :param new_price: new_price for the product
        :return: Nothing
        """
        pass

    @staticmethod
    def compare_price_for_product(product_id, compare_price):
        """
        Method will tkae the product_id and get the product.
        Then the price will be compared to the new_price given
        :param product_id: shopify id for the product
        :param compare_price: price to compare to
        :return: Nothing
        """
        pass

    @staticmethod
    def lookup_product(product_id):
        """
        Method will take the product_id and see if the
        product exists in the shopify database or now
        :param product_id: shopify id for the product
        :return: 1 if exists, -1 if not
        """
        pass

    @staticmethod
    def lookup_margin_for_product(product_id):
        """
        Method will take the product_id and give back
        the margin of profit that we are getting

        The formula for this is
        (curr_price - map_price) / (map_price)
        :param product_id: shopify id for the product
        :return: profit margin
        """
        pass

    @staticmethod
    def lookup_product_instock(product_id):
        """
        Method will take the product_id and say
        whether the product is in stock or not
        :param product_id: shopify id for the product
        :return: 1 if in stock, 0 if not
        """
        pass

    @staticmethod
    def send_newsletter(newsletter):
        """
        Prototype method

        I would like this method to be able to take a message
        from Mark and send it to everyone. This would be if there
        is a big sale and he wants to tell everyone so they can go
        buy! This would be really streamline and all can be done from
        the phone I believe.

        Just something to thing about that would be awesome
        :param newsletter: text that will be sent in the newsletter
        :return: Nothing
        """
        pass

    @staticmethod
    def lookup_product_info(product_id):
        """
        Method will take the product_id and get
        all of the info about the product. This will
        use the __str__ method from the variants and just
        return that.
        :param product_id: shopify id for the product
        :return: str representation of the product
        """
        pass

    @staticmethod
    def lookup_amount_of_product_sold(product_id):
        """
        Method will take the product_id and return
        the number sold of that product overall.
        :param product_id: shopify id for the product
        :return: number of product sold
        """
        pass

    @staticmethod
    def overall_money_made():
        """
        Simple method that just returns how much money
        has been made net from the website. Kind of vague
        but would be cool to see on a graph
        :return: total net money made
        """
        pass
