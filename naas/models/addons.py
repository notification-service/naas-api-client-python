import naas
from naas.configuration import Configuration
from naas.errors import InvalidRequestError, RecordNotFoundError
from naas.models.addon import Addon as AddonModel
from naas.models.error import Error


class Addons(object):
    """

    Addons
    ===============

    This returns an instance of the Addons model
    """
    COLUMNS = ['ID', 'System Type', 'Name', 'Description', 'Supports Multiple', 'Default']

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: AddonModel(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    @classmethod
    def headings(cls):
        """
        Helper to retrieve the headings collection
        """
        return cls.COLUMNS

    @classmethod
    def list(cls, params=None):
        """
        Helper method to retrieve from the request
        :param params: dict
        :return: Addons
        """
        if params is None:
            params = {}

        request = naas.requests.Addons.list(params)

        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
        else:
            Configuration(
                {
                    "logger": ("Failure retrieving the addons "
                               f"{request.status_code}")
                }
            )
        return cls(klass_attributes)

    @staticmethod
    def retrieve(_id, params=None):
        """
        Helper method to retrieve from the request
        :param _id: str
        :param params: dict
        :return: Addon
        """
        if params is None:
            params = {}

        request = naas.requests.Addons.retrieve(_id, params)

        if request:
            return AddonModel(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {_id}")
            return

        Configuration(
            {"logger": f"Failure retrieving the addon {request.status_code}"}
        )
