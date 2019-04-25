import iso8601

from naas.models.links import Links


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

    def confirmed_at_value(self):
        """Returns confirmation date value for the record"""
        return self.attributes.get('confirmed_at')

    def confirmed_at(self):
        """Returns the confirmed at timestamp value"""
        try:
            return iso8601.parse_date(self.confirmed_at_value())
        except iso8601.iso8601.ParseError as e:
            None

    def created_at(self):
        """Returns the created at timestamp value"""
        return iso8601.parse_date(self.attributes.get('created_at'))

    def updated_at(self):
        """Returns the updated at timestamp value"""
        return iso8601.parse_date(self.attributes.get('updated_at'))

    def links_attributes(self):
        """Returns the links attributes"""
        return self.attributes.get('links', [])

    def links(self):
        """Returns links"""
        return Links(self.links_attributes())
