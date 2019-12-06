"""
Tags Class

Class I created in order to keep track of tags and easily edit them
"""


class Tags:
    def __init__(self):
        """
        __init__ dunder method for Tags Class
        """
        self.tags = []
        self.num_of_tags = 0

    def add_tag(self, tag):
        """
        Add Tag method to add a tag
        :param tag: tag to add to array
        :return: nothing
        """
        self.tags.append(tag)
        self.num_of_tags += 1

    def is_a_tag(self, tag):
        """
        See if a tag exists
        :param tag: tag we are checking
        :return: if that tag exists
        """
        if tag in self.tags:
            return True
        else:
            return False

    def tags_to_string(self):
        """
        Converts self.tags to a string for Shopify.Product.tags
        :return: string version of self.tags
        """
        shopify_str = ''
        for t in self.tags:
            shopify_str += t + ","
        # include everything except end (the extra comma)
        return shopify_str[:-1]

    def string_to_tags(self, tags_string):
        """
        Converts Shopify.Product.tags to a array for self.tags
        :param tags_string:
        :return: Nothing
        """
        self.tags = tags_string.split(',')
