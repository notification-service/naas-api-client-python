import iso8601


class AccountSetting(object):
    """

    Account Setting
    ===============

    This returns an instance of the account domain model
    """

    def __init__(self, attributes={}):
        self.attributes = attributes

    def send_grid_webhook_token(self):
        """Returns the send grid webhook token"""
        return self.attributes.get('send_grid_webhook_token')

    def send_grid_webhook_url(self):
        """Returns the send grid webhook url"""
        return self.attributes.get('send_grid_webhook_url')

    def created_at(self):
        """Returns the created at timestamp value"""
        return iso8601.parse_date(self.attributes.get('created_at'))

    def updated_at(self):
        """Returns the updated at timestamp value"""
        return iso8601.parse_date(self.attributes.get('updated_at'))
