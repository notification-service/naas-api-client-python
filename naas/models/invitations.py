import naas
from naas.configuration import Configuration
from naas.errors import InvalidRequestError, RecordNotFoundError
from naas.models.invitation import Invitation as InvitationModel
from naas.models.error import Error


class Invitations(object):
    """

    Invitations
    ===============

    This returns an instance of the Invitations model
    """
    COLUMNS = ['ID', 'System Type', 'Name', 'Description', 'Supports Multiple', 'Default']

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: InvitationModel(r), self.collection)

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
        :return: Invitations
        """
        if params is None:
            params = {}

        request = naas.requests.Invitations.list(params)

        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
        else:
            Configuration(
                {
                    "logger": ("Failure retrieving the invitations "
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
        :return: Invitation
        """
        if params is None:
            params = {}

        request = naas.requests.Invitations.retrieve(_id, params)

        if request:
            return InvitationModel(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {_id}")
            return

        Configuration(
            {"logger": f"Failure retrieving the invitation {request.status_code}"}
        )

    @staticmethod
    def accept(_id, params=None):
        """
        Helper method to accept the invitation

        :param _id: str
        :param params: dict
        :return: Invitation
        """
        if params is None:
            params = {}

        request = naas.requests.Invitations.accept(_id, params)

        if request:
            return InvitationModel(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with {_id}")
            return
        elif request.status_code == 422:
            raise RecordNotFoundError(f"Unprocessable record with {_id}")
            return

        Configuration(
            {"logger": f"Failure accepting the invitation {request.status_code}"}
        )

    @staticmethod
    def decline(_id, params=None):
        """
        Helper method to decline the invitation

        :param _id: str
        :param params: dict
        :return: Invitation
        """
        if params is None:
            params = {}

        request = naas.requests.Invitations.decline(_id, params)

        if request:
            return InvitationModel(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with {_id}")
            return
        elif request.status_code == 422:
            raise RecordNotFoundError(f"Unprocessable record with {_id}")
            return

        Configuration(
            {"logger": f"Failure accepting the invitation {request.status_code}"}
        )
