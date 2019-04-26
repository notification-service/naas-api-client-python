import iso8601
from naas.models.links import Links


class AccountSmtpSetting(object):
    """

    Account SMTP Setting
    ===============

    This returns an instance of the Account Smtp Setting domain model
    """

    def __init__(self, attributes={}):
        self.attributes = attributes

    def id(self):
        """Returns the id"""
        return self.attributes.get('id')

    def name(self):
        """Returns the name"""
        return self.attributes.get('name')

    def description(self):
        """Returns the description"""
        return self.attributes.get('description')

    def user_name(self):
        """Returns the user_name"""
        return self.attributes.get('user_name')

    def address(self):
        """Returns the address"""
        return self.attributes.get('address')

    def domain(self):
        """Returns the domain"""
        return self.attributes.get('domain')

    def port(self):
        """Returns the port"""
        return self.attributes.get('port')

    def authentication_type_value(self):
        """Returns the authentication type value"""
        return self.attributes.get('authentication_type_value')

    def is_starttls_auto_enabled(self):
        """Returns true if start TLS auto is enabled"""
        return self.attributes.get('is_starttls_auto_enabled')

    def is_primary(self):
        """Returns true if this is the primary"""
        return self.attributes.get('is_primary')

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
        return Links(self.links_attributes())
