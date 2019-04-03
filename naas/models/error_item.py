"""

Error Item
===============

This returns an instance of the Error Item domain model
"""


class ErrorItem(object):
    def __init__(self, attributes={}):
        self.attributes = attributes

    def code(self):
        """Returns the custom code of the specific error"""
        return self.attributes.get('code')

    def field(self):
        """Returns the corresponding field"""
        return self.attributes.get('code')

    def message(self):
        """Returns the message"""
        return self.attributes.get('message')

    def full_message(self):
        """Returns the fully formatted message"""
        return self.message
