import iso8601

from naas.models.links import Links


class Invitation(object):
    """

    Invitation
    ===============

    This returns an instance of the Invitation domain model
    """

    def __init__(self, attributes):
        self.attributes = attributes

    def id(self):
        """Returns the invitation id"""
        return self.attributes.get('id')

    def accepted_invitation_id(self):
        """Returns the accepted invitation id"""
        return self.attributes.get('accepted_invitation_id')

    def account_addon_id(self):
        """Returns the account addon id"""
        return self.attributes.get('account_addon_id')

    def sender_subscriber_id(self):
        """Returns the sender subscriber id"""
        return self.attributes.get('sender_subscriber_id')

    def sender(self):
        """Returns the sender address"""
        return self.attributes.get('sender')

    def subscriber_id(self):
        """Returns the subscriber id"""
        return self.attributes.get('subscriber_id')

    def recipient(self):
        """Returns the recipient address"""
        return self.attributes.get('recipient')

    def code(self):
        """Returns the code"""
        return self.attributes.get('code')

    def is_pending(self):
        """Returns true if pending"""
        return self.attributes.get('is_pending')

    def is_accepted(self):
        """Returns true if accepted"""
        return self.attributes.get('is_accepted')

    def is_declined(self):
        """Returns true if declined"""
        return self.attributes.get('is_declined')

    def has_accepted_other(self):
        """Returns true if it has been auto accepted by another"""
        return self.attributes.get('has_accepted_other')

    def accepted_at_value(self):
        """Returns the accepted at timestamp value"""
        return self.attributes.get('accepted_at', None)

    def accepted_at(self):
        """Returns the accepted at timestamp"""
        date_value = self.accepted_at_value()
        try:
            return iso8601.parse_date(date_value)
        except iso8601.iso8601.ParseError as e:
            return None
        except ValueError as e:
            return None

    def declined_at_value(self):
        """Returns the declined at timestamp value"""
        return self.attributes.get('declined_at', None)

    def declined_at(self):
        """Returns the declined at timestamp"""
        date_value = self.declined_at_value()
        try:
            return iso8601.parse_date(date_value)
        except iso8601.iso8601.ParseError as e:
            return None
        except ValueError as e:
            return None

    def created_at_value(self):
        """Returns the created at timestamp value"""
        return self.attributes.get('created_at')

    def created_at(self):
        """Returns the created at timestamp"""
        date_value = self.created_at_value()
        try:
            return iso8601.parse_date(date_value)
        except ValueError as e:
            return None

    def updated_at_value(self):
        """Returns the updated at timestamp value"""
        return self.attributes.get('updated_at')

    def updated_at(self):
        """Returns the updated at timestamp"""
        date_value = self.updated_at_value()
        try:
            return iso8601.parse_date(date_value)
        except ValueError as e:
            return None

    def links_attributes(self):
        """Returns the links collection attributes"""
        return self.attributes.get('links', [])

    def links(self):
        """Returns links"""
        return Links(self.links_attributes())
