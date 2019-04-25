from naas.models import ErrorItems

class Error(object):
    """

    Error
    ===============

    This returns an instance of the Error domain model
    """

    def __init__(self, attributes={}):
        self.attributes = attributes

    def status(self):
        """Returns the HTTP status of the error"""
        return self.attributes.get('status')

    def message(self):
        """Returns the HTTP message of the error"""
        return self.attributes.get('message')

    def errors_attributes(self):
        """Returns the errors attributes collection"""
        return self.attributes.get('errors', [])

    def errors(self):
        """Returns the collection of ErrorItems"""
        return ErrorItems(self.errors_attributes)

    def full_messages(self):
        """Delegate to the error for full messages"""
        return self.errors.full_messages
