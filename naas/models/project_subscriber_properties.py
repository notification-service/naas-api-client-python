import naas
from naas.configuration import Configuration
from naas.errors import InvalidRequestError, RecordNotFoundError
from naas.models.project_subscriber_property import ProjectSubscriberProperty


class ProjectSubscriberProperties(object):
    """

    Project Subscriber Properties
    ===============

    This returns an instance of the project subscriber properties
    """

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: ProjectSubscriberProperty(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    @classmethod
    def list_by_project_id_and_project_subscriber_id(
            cls, project_id, project_subscriber_id, params=None):

        if params is None:
            params = {}

        request = naas.requests.ProjectSubscriberProperties.list_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, params)

        if request:
            return cls(request.json().get('data'))

        Configuration(
            {
                "logger": ("Failure retrieving the property subscriber properties "
                           f"{request.status_code}")
            }
        )

    @staticmethod
    def retrieve_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, _id, params=None):

        if params is None:
            params = {}

        request = naas.requests.ProjectSubscriberProperties.retrieve_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, _id, params)

        if request:
            return ProjectSubscriberProperty(request.json().get('data'))

        Configuration(
            {
                "logger": ("Failure retrieving the property subscriber property "
                           f"{request.status_code}")
            }
        )

    @staticmethod
    def create_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, params=None):

        if params is None:
            params = {}

        request = naas.requests.ProjectSubscriberProperties.create_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, params)

        if request:
            return ProjectSubscriberProperty(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages()}")

        Configuration({"logger": f"{failure_message}"})
        raise InvalidRequestError(failure_message)

    @staticmethod
    def update_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, _id, params=None):

        if params is None:
            params = {}

        request = naas.requests.ProjectSubscriberProperties.update_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, _id, params)

        if request:
            return ProjectSubscriberProperty(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages()}")

        Configuration({"logger": f"{failure_message}"})
        raise InvalidRequestError(failure_message)
