from nass.configuration import Configuration
from naas.errors import InvalidRequestError, RecordNotFoundError
from nass.models import EmailNotification, Error
from naas.requests import EmailNotifications


class EmailNotifications(object):
    """

    Email Notifications
    ===============

    This returns an instance of the email notifications model
    """

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: EmailNotification(r), self.collection)

    @staticmethod
    def deliver(id, params=None):
        if params is None:
            params = {}

        request = EmailNotifications.deliver(id, params)

        if request:
            Configuration.logger.info(
                f"Delivered email notification {request.status_code}")
        else:
            Configuration.logger.info(
                "Failure delivering the email notification "
                f"{request.status_code}"
            )

    @classmethod
    def list(params=None):
        if params is None:
            params = {}

        request = EmailNotifications.list(params)
        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
        else:
            Configuration.logger.error(
                "Failure retrieving the email notifications "
                f"{request.status_code}"
            )
        return cls(klass_attributes)

    @staticmethod
    def retrieve(id, params=None):
        if params is None:
            params = {}

        request = EmailNotifications.retrieve(id, params)

        if request:
            return EmailNotification(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {id}")
            return

        Configuration.logger.error(
            f"Failure retrieving the email notification {request.status_code}")

    @staticmethod
    def create(params=None):
        if params is None:
            params = {}

        request = EmailNotifications.create(params)

        if request:
            return EmailNotification(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages}")

        Configuration.logger.error(failure_message)
        raise InvalidRequestError(failure_message)
