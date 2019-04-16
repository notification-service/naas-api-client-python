from nass.configuration import Configuration
from nass.models import Account
from naas.requests import Accounts


class Accounts(object):
    """

    Accounts
    ===============

    This returns an instance of the accounts
    """

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: Account(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    @staticmethod
    def retrieve(id, params=None):
        if params is None:
            params = {}

        request = Accounts.retrieve(params)

        if request:
            return Account(request.json().get('data'))

        Configuration.logger.error(
            f"Failure retrieving the account {request.status_code}")
