import naas
from naas.models.data_type import DataType


class DataTypes(object):
    """

    DataTypes
    ===============

    This returns an instance of the data_types model
    """

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: DataType(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    @classmethod
    def list(cls, params=None):

        if not params:
            params = {}

        request = naas.requests.DataTypes.list(params)

        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
            return cls(klass_attributes)

        Configuration(
            {
                "logger": ("Failure retrieving the data types "
                           f"{request.status_code}")
            }
        )

    @staticmethod
    def retrieve(_id, params):
        if not params:
            params = {}

        request = naas.requests.DataTypes.retrieve(_id, params)

        if request:
            return DataType(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {_id}")
            return

        Configuration(
            {
                "logger": ("Failure retrieving the data type "
                           f"{request.status_code}")
            }
        )

    def to_a(self):
        pass

    def to_option(self):
        pass
