import datetime

from naas.models import Links


class SubscriberEmailAddress(object):
    """

    Subscriber Email Address
    ===============

    This returns an instance of the Subscriber Email Address domain model
    """

    def __init__(self, attributes={}):
        self.attributes = attributes

    def id(self):
        """Returns the id"""
        return self.attributes.get('id')

    def subscriber_id(self):
        """Returns the subscriber id"""
        return self.attributes.get('subscriber_id')

    def email_address(self):
        """Returns the subscriber email address"""
        return self.attributes.get('email_address')

    def email_address_hash(self):
        """Returns the subscriber email address hash"""
        return self.attributes.get('email_address_hash')

    def confirmation_code(self):
        """Returns confirmation code for the record"""
        return self.attributes.get('confirmation_code')

    def confirmed_at(self):
        """Returns the confirmed at timestamp value"""
        try:
          return datetime.datetime.strptime(
            self.attributes.get('confirmed_at'), '%Y-%m-%dT%H:%M:%S%z')
        except TypeError as e:
          None

    def created_at(self):
        """Returns the created at timestamp value"""
        return datetime.datetime.strptime(
            self.attributes.get('created_at'), '%Y-%m-%dT%H:%M:%S%z')

    def updated_at(self):
        """Returns the updated at timestamp value"""
        return datetime.datetime.strptime(
            self.attributes.get('updated_at'), '%Y-%m-%dT%H:%M:%S%z')

    def links_attributes(self):
        """Returns the links attributes"""
        return self.attributes.get('links', [])

    def links(self):
        """Returns links"""
        return Links(self.links_attributes())
