import naas
from naas.configuration import Configuration
from naas.models.email_notification_status import EmailNotificationStatus


class EmailNotificationStatuses(object):
    """

    Email Notification Statuses
    ===============

    This returns an instance of the email notification statuses model
    """

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: EmailNotificationStatus(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    @staticmethod
    def retrieve_by_email_notification_id(email_notification_id, params=None):
        """
        Helper method to retrieve from the request
        :param email_notification_id: str
        :param params: dict
        :return: EmailNotificationStatus
        """
        if params is None:
            params = {}

        request = naas.requests.EmailNotificationStatuses.retrieve_by_email_notification_id(
            email_notification_id, params)

        if request:
            return EmailNotificationStatus(request.json().get('data'))

        Configuration(
            {
                "logger": (f"Failure retrieving the email notification "
                           "status {request.status_code}")
            }
        )
