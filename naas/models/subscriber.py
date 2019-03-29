"""

Subscriber
===============

This returns an instance of the Subscriber domain model
"""
from naas.models import Links


class Subscriber(object):
    def __init__(self, attributes={}):
        self.attributes = attributes

    def id(self):
        """Returns the subscriber id"""
        return self.attributes.get('id')

    def first_name(self):
        """Returns the subscriber first_name"""
        return self.attributes.get('first_name')

    def last_name(self):
        """Returns the subscriber last_name"""
        return self.attributes.get('last_name')

    def full_name(self):
        """Returns the subscriber full_name"""
        return f'{self.first_name} {self.last_name}'

    def email(self):
        """Returns the subscriber email"""
        return self.attributes.get('email')

    def created_at(self):
        """Returns the created at timestamp value"""
        return self.attributes.get('created_at')

    def updated_at(self):
        """Returns the updated at timestamp value"""
        return self.attributes.get('updated_at')

    def links_attributes(self):
        """Returns the links collection attributes"""
        return self.attributes.get('links', [])

    def subscriber_email_addresses_attributes(self):
        """Returns the associated email addresses attributes"""
        return self.attributes.get('subscriber_email_addreses', [])

    def links(self):
        return Links(self.links_attributes())
