import naas
from naas.configuration import Configuration
from naas.errors import InvalidRequestError, RecordNotFoundError
from naas.models.campaign import Campaign
from naas.models.error import Error


class Campaigns(object):
    """

    Campaigns
    ===============

    This returns an instance of the campaigns model
    """

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: Campaign(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    @classmethod
    def list_by_project_id(cls, project_id, params=None):
        """
        Helper method to retrieve from the request
        :param project_id: str
        :param params: dict
        :return: Campaigns
        """
        if params is None:
            params = {}

        request = naas.requests.Campaigns.list_by_project_id(
            project_id, params)

        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
        else:
            Configuration(
                {
                    "logger": ("Failure retrieving the campaigns "
                               f"{request.status_code}")
                }
            )

        return cls(klass_attributes)

    @staticmethod
    def retrieve_by_project_id(project_id, _id, params=None):
        """
        Helper method to retrieve from the request
        :param project_id: str
        :param _id: str
        :param params: dict
        :raises RecordNotFoundError
        :return: Campaign
        """
        if params is None:
            params = {}

        request = naas.requests.Campaigns.retrieve_by_project_id(
            project_id, _id, params)

        if request:
            return Campaign(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {_id}")
            return

        Configuration(
            {
                "logger": ("Failure retrieving the campaign "
                           f"{request.status_code}")
            }
        )

    @staticmethod
    def create_by_project_id(project_id, params=None):
        """
        Create a new campaign
        :param project_id: str
        :param params: dict
        :raises InvalidRequestError
        :return: Campaign
        """
        if params is None:
            params = {}

        request = naas.requests.Campaigns.create_by_project_id(
            project_id, params)

        if request:
            return Campaign(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages}")

        Configuration({"logger": f"{failure_message}"})
        raise InvalidRequestError(failure_message)

    @staticmethod
    def update_by_project_id(project_id, _id, params=None):
        """
        Update an existing campaign
        :param project_id: str
        :param _id: str
        :param params: dict
        :return: Campaign
        """
        if params is None:
            params = {}

        request = naas.requests.Campaigns.update_by_project_id(
            project_id, _id, params)

        if request:
            return Campaign(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages}")

        Configuration({"logger": f"{failure_message}"})
        raise InvalidRequestError(failure_message)
