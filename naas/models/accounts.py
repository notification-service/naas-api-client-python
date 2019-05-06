import naas
from naas.configuration import Configuration
from naas.models.account import Account


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
    def retrieve(params=None):
        """
        Helper method to retrieve from the request
        :param params: dict
        :return: Account
        """
        if params is None:
            params = {}

        request = naas.requests.Accounts.retrieve(params)

        if request:
            return Account(request.json().get('data'))

        Configuration(
            {
                "logger": ("Failure retrieving the account "
                           f"{request.status_code}")
            }
        )
