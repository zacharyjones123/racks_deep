class ShopifyProduct:
    def __init__(self, tags, title, options, vendor, product_type, body_html):
        """

        :param product_id: the shopify id of the product (used for shopify lookup)
        :param tags: list of all tags to put on the shopify product
        :param title: Title of the product
        :param product_variants: All variants of this product (ShopifyProductVariant)
        :param options: options for variants (ex. [{'name': 'Tire Size'}, {'name': 'Bolt Pattern'}, {'name': 'Offset'}] )
        :param vendor: vendor that is selling (Racks Deep default)
        :param product_type: type of the product
        :param body_html: What is shown in the description

        """
        self.product_id = None
        self.tags = tags
        self.title = title
        self.product_variants = []
        self.options = options
        self.vendor = vendor
        self.product_type = product_type
        self.body_html = body_html

    def __eq__(self, other):
        if self.product_id != other.product_id:
            return False
        else:
            return True

    def __str__(self):
        return f"Product Title: {self.title}\nProduct Id: {self.product_id}\n"

    def __repr__(self):
        return f"Product Title: {self.title}\nProduct Id: {self.product_id}\n"


class ShopifyProductVariant:
    def __init__(self, price, option1, option2, option3, sku, inventory_quantity, weight, image_url):
        self.price = price
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.quantity = 1
        self.sku = sku
        self.position = 1
        self.inventory_policy = "deny"
        self.fulfillment_service = "manual"
        self.inventory_management = "shopify"
        self.inventory_quantity = inventory_quantity
        self.taxable = True
        self.weight = weight
        self.weight_unit = "g"
        self.requires_shipping = True
        self.image_url = image_url
