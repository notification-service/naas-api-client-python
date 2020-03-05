import naas
from naas.configuration import Configuration
from naas.errors import InvalidRequestError
from naas.models.error import Error
from naas.models.project import Project
from naas.models.projects import Projects
#from naas.models.project_subscriber import ProjectSubscriber as ProjectSubscriberModel
#from naas.models.project_subscribers import ProjectSubscribers as ProjectSubscribersModel


class ProjectSubscriberProfile(object):
    """

    Project Subscriber Profile
    ===============

    This returns an instance of the Project Subscriber Profile domain model
    """

    def __init__(self, attributes={}):
        self.attributes = attributes
        self.project_id = self.attributes.get('project_id')
        self.project_subscriber_id = self.attributes.get('project_subscriber_id')
        for key, value in self.attributes.items():
            setattr(self, key, value)
            getattr(self, key)

    @classmethod
    def retrieve_by_project_id_and_project_subscriber_id(
            cls, project_id, project_subscriber_id, params=None):
        """
        Helper method to retrieve from the request
        :param project_id: str
        :param project_subscriber_id: str
        :param params: dict
        :return: ProjectSubscriberProfile
        """
        if not params:
            params = {}

        request = naas.requests.ProjectSubscriberProfiles.retrieve_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, params
        )

        if request:
            data = request.json().get('data')
            data.update({'project_id': project_id})
            data.update({'project_subscriber_id': project_subscriber_id})
            return cls(data)

        Configuration(
            {
                "logger": ("Failure retrieving the project subscriber profile "
                           f"{request.status_code}")
            }
        )

    @classmethod
    def update_by_project_id_and_project_subscriber_id(
            cls, project_id, project_subscriber_id, params=None):
        """
        Update an existing project subscriber profile
        :param project_id: str
        :param project_subscriber_id: str
        :param params: dict
        :return: ProjectSubscriberProfile
        """
        if not params:
            params = {}

        request = naas.requests.ProjectSubscriberProfiles.update_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, params
        )

        if request:
            data = request.json().get('data')
            data.update({'project_id': project_id})
            data.update({'project_subscriber_id': project_subscriber_id})
            return cls(data)

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages()}")
        Configuration({"logger": f"{failure_message}"})
        raise InvalidRequestError(failure_message)

    def project_id(self):
        """Returns the associated project id"""
        return self.attributes.get('project_id')

    def project_attributes(self):
        """Returns the project attributes"""
        return self.attributes.get('project', {})

    def project(self):
        """Returns an instance of the project"""
        if self.project_attributes():
            return Project(self.project_attributes())
        return Projects.retrieve(self.project_id())

    def project_subscriber_id(self):
        """Returns the project subscriber id"""
        return self.attributes.get('project_subscriber_id')

    def project_subscriber_attributes(self):
        """Returns the project subscriber attributes"""
        return self.attributes.get('project_subscriber', {})

    def project_subscriber(self):
        """Returns an instance of the project subscriber"""
        if self.project_subscriber_attributes():
            return ProjectSubscriberModel(self.project_subscriber_attributes())
        return ProjectSubscribersModel.retrieve_by_project_id(
            self.project_id(), self.project_subscriber_id())
