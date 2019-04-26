import naas
from naas.configuration import Configuration
from naas.errors import InvalidRequestError, RecordNotFoundError
from naas.models.email_notification import EmailNotification
from naas.models.error import Error


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
    def deliver(_id, params=None):
        """
        Deliver the email notification
        :param _id: str
        :param params: dict
        """
        if params is None:
            params = {}

        request = naas.requests.EmailNotifications.deliver(_id, params)

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
        """
        Helper method to retrieve from the request
        :param params: dict
        :return: EmailNotifications
        """
        if params is None:
            params = {}

        request = naas.requests.EmailNotifications.list(params)
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
    def retrieve(_id, params=None):
        """
        Helper method to retrieve from the request
        :param _id: str
        :param params: dict
        :raises RecordNotFoundError
        :return: EmailNotification
        """
        if params is None:
            params = {}

        request = naas.requests.EmailNotifications.retrieve(_id, params)

        if request:
            return EmailNotification(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {_id}")
            return

        Configuration.logger.error(
            f"Failure retrieving the email notification {request.status_code}")

    @staticmethod
    def create(params=None):
        """
        Helper method to retrieve from the request
        :param params: dict
        :raises InvalidRequestError
        :return: EmailNotification
        """
        if params is None:
            params = {}

        request = naas.requests.EmailNotifications.create(params)

        if request:
            return EmailNotification(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages}")

        Configuration.logger.error(failure_message)
        raise InvalidRequestError(failure_message)
