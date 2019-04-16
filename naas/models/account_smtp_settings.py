from nass.configuration import Configuration
from naas.errors import InvalidRequestError, RecordNotFoundError
from nass.models import AccountSetting, Error
from naas.requests import AccountSmtpSettings


class AccountSmtpSettings(object):
    """

    Account Smtp Settings
    ===============

    This returns an instance of the account smtp settings domain model
    """

    def __init__(self, collection):
        self.collection = list(collection)

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
        if params is None:
            params = {}
        request = AccountSmtpSettings.list(params)
        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
        else:
            Configuration.logger.error(
                "Failure retrieving the smtp settings {request.status_code}")
        return cls(klass_attributes)

    @staticmethod
    def retrieve(id, params=None):
        if params is None:
            params = {}

        request = AccountSmtpSettings.retrieve(id, params)

        if request:
            return AccountSmtpSetting(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {id}")

        Configuration.logger.error(
            f"Failure retrieving the smtp setting {request.status_code}")

    @staticmethod
    def create(params=None):
        if params is None:
            params = {}

        request = AccountSmtpSettings.create(params)

        if request:
            return AccountSmtpSettings(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages.inspect}")

        Configuration.logger.error(failure_message)
        raise InvalidRequestError(failure_message)
