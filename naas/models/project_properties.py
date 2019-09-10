import naas
from naas.models.project_property import ProjectProperty


class ProjectProperties(object):
    """

    Project Properties
    ===============

    This returns an instance of the ProjectProperties model
    """
    COLUMNS = [
        'ID', 'Project ID', 'Data Type ID', 'Name', 'Key Name', 'Description',
        'Subscriber Editable', 'Subscriber Viewable', 'Created At'
    ]

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: ProjectProperty(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    def headings(self):
        pass

    def headings(cls):
        pass

    @classmethod
    def list_by_project_id(cls, project_id, params=None):
        if not params:
            params = {}

        request = naas.requests.ProjectProperties.list_by_project_id(
            project_id, params)

        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
            return cls(klass_attributes)

        Configuration(
            {
                "logger": ("Failure retrieving the project properties "
                           f"{request.status_code}")
            }
        )

    @staticmethod
    def retrieve_by_project_id(project_id, _id, params=None):
        if not params:
            params = {}

        request = naas.requests.ProjectProperties.retrieve_by_project_id(
            project_id, _id, params)

        if request:
            return ProjectProperty(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {_id}")
            return

        Configuration(
            {
                "logger": ("Failure retrieving the project property "
                           f"{request.status_code}")
            }
        )

    @staticmethod
    def create_by_project_id(project_id, params=None):
        if not params:
            params = {}

        request = naas.requests.ProjectProperties.create_by_project_id(
            project_id, params)

        if request:
            return ProjectProperty(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages()}")

        Configuration({"logger": f"{failure_message}"})
        raise InvalidRequestError(failure_message)

    @staticmethod
    def update_by_project_id(project_id, _id, params=None):
        if not params:
            params = {}

        request = naas.requests.ProjectProperties.update_by_project_id(
            project_id, _id, params)

        if request:
            return ProjectProperty(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages()}")

        Configuration({"logger": f"{failure_message}"})
        raise InvalidRequestError(failure_message)

    def to_a(self):
        pass

    def subscriber_viewable(self):
        pass

    def subscriber_editable(self):
        pass
