"""

Account Setting
===============

This returns an instance of the account domain model
"""
import datetime


class AccountSetting(object):
    def __init__(self, attributes={}):
        self.attributes = attributes

    def send_grid_webhook_token(self):
        """Returns the send grid webhook token"""
        return self.attributes.get('send_grid_webhook_token')

    def send_grid_webhook_url(self):
        """Returns the send grid webhook url"""
        return self.attributes.get('send_grid_webhook_url')

    def created_at(self):
        """Returns the created at timestamp"""
        return datetime.datetime.strptime(
            self.attributes.get('created_at'), '%Y-%m-%dT%H:%M:%S%z')

    def updated_at(self):
        """Returns the updated at timestamp"""
        return datetime.datetime.strptime(
            self.attributes.get('updated_at'), '%Y-%m-%dT%H:%M:%S%z')
