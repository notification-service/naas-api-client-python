import iso8601

from naas.models.links import Links


class EmailNotificationStatus(object):
    """

    Email Notification Status
    ===============

    This returns an instance of the Email Notification Status domain model
    """

    def __init__(self, attributes={}):
        self.attributes = attributes

    def id(self):
        """Returns the subscriber id"""
        return self.attributes.get('id')

    def email_notification_id(self):
        """Returns the email notification id"""
        return self.attributes.get('email_notification_id')

    def status_name(self):
        """Returns the status_name"""
        return self.attributes.get('status_name')

    def started_at(self):
        """ Returns the started timestamp"""
        return iso8601.parse_date(self.attributes.get('started_at'))

    def elapsed_seconds(self):
        """Returns the elapsed seconds"""
        return self.attributes.get('elapsed_seconds')

    def elapsed_duration(self):
        """Returns the elapsed duration"""
        return self.attributes.get('elapsed_duration')

    def created_at(self):
        """Returns the created at timestamp"""
        return iso8601.parse_date(self.attributes.get('created_at'))

    def updated_at(self):
        """Returns the updated at timestamp"""
        return iso8601.parse_date(self.attributes.get('updated_at'))

    def links_attributes(self):
        """Returns the links collection attributes"""
        return self.attributes.get('links', [])

    def links(self):
        """Returns links"""
        return Links(self.links_attributes())
