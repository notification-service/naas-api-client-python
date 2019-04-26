import naas
from naas.configuration import Configuration
from naas.errors import InvalidRequestError, RecordNotFoundError
from naas.models.account_setting import AccountSetting
from naas.models.error import Error


class AccountSmtpSettings(object):
    """

    Account Smtp Settings
    ===============

    This returns an instance of the account smtp settings domain model
    """

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: AccountSmtpSetting(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    @classmethod
    def list(params=None):
        """
        Helper method to retrieve from the request
        :param params: dict Attributes
        :return: AccountSmtpSettings
        """
        if params is None:
            params = {}
        request = naas.requests.AccountSmtpSettings.list(params)
        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
        else:
            Configuration.logger.error(
                "Failure retrieving the smtp settings {request.status_code}")
        return cls(klass_attributes)

    @staticmethod
    def retrieve(_id, params=None):
        """
        Helper method to retrieve from the request
        :param _id: str
        :param params: dict
        :raises RecordNotFoundError
        :return: AccountSmtpSetting
        """
        if params is None:
            params = {}

        request = naas.requests.AccountSmtpSettings.retrieve(_id, params)

        if request:
            return AccountSmtpSetting(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {_id}")
            return

        Configuration.logger.error(
            f"Failure retrieving the smtp setting {request.status_code}")

    @staticmethod
    def create(params=None):
        """
        Create a new SMTP setting
        :param params: dict
        :raises InvalidRequestError
        :return: AccountSmtpSetting
        """
        if params is None:
            params = {}

        request = naas.requests.AccountSmtpSettings.create(params)

        if request:
            return AccountSmtpSetting(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages}")

        Configuration.logger.error(failure_message)
        raise InvalidRequestError(failure_message)
