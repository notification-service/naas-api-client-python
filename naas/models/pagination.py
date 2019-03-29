"""

Pagination
===============

This returns an instance of the pagination domain model
"""


class Pagination(object):
    def __init__(self, attributes={}):
        self.attributes = attributes

    def page(self):
        """Returns the current page"""
        return int(self.attributes.get('page'))

    def per_page(self):
        """Returns the number of items per page"""
        return int(self.attributes.get('per_page'))

    def total(self):
        """Returns the total number of entries"""
        return int(self.attributes.get('total'))

    def maximum_per_page(self):
        """Returns the maximum per page"""
        return int(self.attributes.get('maximum_per_page'))

    def total_pages(self):
        """Returns the total number of pages"""
        return (self.total() / self.per_page())
