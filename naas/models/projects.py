from naas.configuration import Configuration
from naas.errors import InvalidRequestError, RecordNotFoundError
from naas.models import Project, Error
from naas.requests import Projects


class Projects(object):
    def __init__(self, collection):
        self.collection = list(collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: Project(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    @staticmethod
    def list(params=None):
        """
        Helper method to retrieve from the request
        :param params: dict
        :return: Projects
        """
        if params is None:
            params = {}

        request = Projects.list(params)

        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
        else:
            Configuration.logger.error(
                "Failure retrieving the projects {request.status_code}"
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

        request = Projects.retrieve(_id, params)

        if request:
            return Project(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {_id}")
            return

        Configuration.logger.error(
            "Failure retrieving the project {request.status_code}"
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

        request = Projects.create(params)

        if request:
            return Project(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages}")

        Configuration.logger.error(failure_message)
        raise InvalidRequestError(failure_message)
