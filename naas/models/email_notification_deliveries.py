import naas
from naas.configuration import Configuration
from naas.models.email_notification_delivery import EmailNotificationDelivery


class EmailNotificationDeliveries(object):
    """

    Email Notification Deliveries
    ===============

    This returns an instance of the email notification deliveries model
    """

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: EmailNotificationDelivery(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    @classmethod
    def list_by_email_notification_id(cls, email_notification_id, params=None):
        """
        Helper method to retrieve from the request
        :param email_notification_id: str
        :param params: dict
        :return: EmailNotificationDeliveries
        """
        if params is None:
            params = {}

        request = naas.requests.EmailNotificationDeliveries.list_by_email_notification_id(
            email_notification_id, params)

        klass_attributes = []

        if klass_attributes:
            klass_attributes = request.json().get('data')
        else:
            Configuration(
                {
                    "logger": ("Failure retrieving the email notification "
                               f"deliveries {request.status_code}")
                }
            )
        return cls(klass_attributes)

    @staticmethod
    def retrieve_by_email_notification_id(email_notification_id, _id, params=None):
        """
        Helper method to retrieve from the request
        :param email_notification_id: str
        :param _id: str
        :param params: dict
        :return: EmailNotificationDelivery
        """
        if params is None:
            params = {}

        request = naas.requests.EmailNotificationDeliveries.retrieve_by_email_notification_id(
            email_notification_id, _id, params)

        if request:
            return EmailNotificationDelivery(request.json().get('data'))

        Configuration(
            {
                "logger": ("Failure retrieving the email notification delivery "
                           f"{request.status_code}")
            }
        )
