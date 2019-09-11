import naas
from naas.models.project_subscriber import ProjectSubscriber


class ProjectSubscribers(object):

    """

    Project Subscribers
    ===============

    This returns an instance of the Project Subscribers model
    """


COLUMNS = ['ID', 'Project ID', 'Subscriber ID', 'Email Addresses', 'Code',
           'Created At']

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: ProjectSubscriber(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    def headings(self):
        """
        Helper to retrieve the headings collection
        """
        return self.COLUMNS

    @classmethod
    def list_by_project_id(cls, project_id, params=None):
        """
        Helper method to retrieve from the request
        :param project_id: str
        :param params: dict
        :return: ProjectSubscribers
        """
        if not params:
            params = {}

        request = naas.requests.ProjectSubscribers.list_by_project_id(
            project_id, params)

        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
            return cls(klass_attributes)

        Configuration(
            {
                "logger": ("Failure retrieving the project subscribers "
                           f"{request.status_code}")
            }
        )

    @staticmethod
    def retrieve_by_project_id(project_id, _id, params=None):
        """
        Helper method to retrieve from the request
        :param project_id: str
        :param _id: str
        :param params: dict
        :raises RecordNotFoundError
        :return: ProjectSubscriber
        """
        if not params:
            params = {}

        request = naas.requests.ProjectSubscribers.retrieve_by_project_id(
            project_id, _id, params)

        if request:
            return ProjectSubscriber(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {_id}")
            return

        Configuration(
            {
                "logger": ("Failure retrieving the project subscriber "
                           f"{request.status_code}")
            }
        )

    @staticmethod
    def create_by_project_id(project_id, params=None):
        """
        Create a new project subscriber
        :param project_id: str
        :param params: dict
        :raises InvalidRequestError
        :return: ProjectSubscriber
        """
        if not params:
            params = {}

        request = naas.requests.ProjectSubscribers.create_by_project_id(
            project_id, params)

        if request:
            return ProjectSubscriber(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages()}")

        Configuration({"logger": f"{failure_message}"})
        raise InvalidRequestError(failure_message)

    def to_a(self):
        """
        Returns the collection serialized as an array
        """
        return list(self.collection)
