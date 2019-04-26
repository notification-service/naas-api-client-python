import iso8601

from naas.models.links import Links


class EmailNotificationDelivery(object):
    """

    Email Notification Delivery
    ===============

    This returns an instance of the Email Notification Delivery domain model
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

    def owner_name(self):
        """Returns the owner name"""
        return self.attributes.get('owner_name')

    def is_started(self):
        """Returns true if this was started"""
        return self.attributes.get('is_started', False)

    def is_completed(self):
        """Returns true if this was completed"""
        return self.attributes.get('is_completed', False)

    def started_at(self):
        """ Returns the started timestamp"""
        return iso8601.parse_date(self.attributes.get('started_at'))

    def completed_at(self):
        """ Returns the completed timestamp"""
        return iso8601.parse_date(self.attributes.get('completed_at'))

    def is_canceled(self):
        """Returns true if this was canceled"""
        return self.attributes.get('is_canceled', False)

    def canceled_at(self):
        """Returns the canceled at timestamp"""
        return iso8601.parse_date(self.attributes.get('canceled_at'))

    def is_errored(self):
        """Returns true if this was errored"""
        return self.attributes.get('is_errored', False)

    def duration(self):
        """Returns the duration of processing time"""
        if self.is_started() and self.is_completed():
            return (self.completed_at() - self.started_at())
        return 0

    def duration_display(self):
        """Returns the duration as a display string"""
        return str(self.duration())

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
