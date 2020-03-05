import naas
from naas.configuration import Configuration
from naas.errors import InvalidRequestError, RecordNotFoundError
from naas.models.project import Project
from naas.models.error import Error


class Projects(object):
    """

    Projects
    ===============

    This returns an instance of the Projects model
    """
    COLUMNS = ['ID', 'Name', 'Description', 'Campaigns', 'Created At']

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: Project(r), self.collection)

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
        :return: Projects
        """
        if params is None:
            params = {}

        request = naas.requests.Projects.list(params)

        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
        else:
            Configuration(
                {
                    "logger": ("Failure retrieving the projects "
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
        :return: Project
        """
        if params is None:
            params = {}

        request = naas.requests.Projects.retrieve(_id, params)

        if request:
            return Project(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {_id}")
            return

        Configuration(
            {"logger": f"Failure retrieving the projects {request.status_code}"}
        )

    @staticmethod
    def create(params=None):
        """
        Create a new project
        :param params: dict
        :return: Project
        """
        if params is None:
            params = {}

        request = naas.requests.Projects.create(params)

        if request:
            return Project(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages()}")

        Configuration({"logger": f"failure_message"})
        raise InvalidRequestError(failure_message)

    def to_a(self):
        """
        Returns the collection serialized as an array
        """
        return list(self.collection)
