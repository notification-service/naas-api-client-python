"""

Account
===============

This returns an instance of the account domain model
"""
import datetime
from naas.models import Links, AccountSetting


class Account(object):
    def __init__(self, attributes={}):
        self.attributes = attributes

    def id(self):
        """Returns the subscriber id"""
        return self.attributes.get('id')

    def name(self):
        """Returns the account name"""
        return self.attributes.get('name')

    def account_setting_attributes(self):
        """Returns the attributes for the account setting"""
        return self.attributes.get('account_setting', {})

    def account_setting(self):
        """Returns the account setting"""
        if self.account_setting_attributes():
            return AccountSetting(self.account_setting_attributes())
        else:
            return AccountSettings.retrieve()

    def created_at(self):
        """Returns the created at timestamp"""
        return datetime.datetime.strptime(
            self.attributes.get('created_at'), '%Y-%m-%dT%H:%M:%S%z')

    def updated_at(self):
        """Returns the updated at timestamp"""
        return datetime.datetime.strptime(
            self.attributes.get('updated_at'), '%Y-%m-%dT%H:%M:%S%z')

    def links_attributes(self):
        """Returns the links collection attributes"""
        return self.attributes.get('links', [])

    def links(self):
        """Returns links"""
        return Links(self.links_attributes())
