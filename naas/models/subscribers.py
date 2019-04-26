import naas
from naas.configuration import Configuration
from naas.errors import InvalidRequestError, RecordNotFoundError
from naas.models.subscriber import Subscriber
from naas.models.error import Error


class Subscribers(object):
    """

    Subscribers
    ===============

    This returns an instance of the Ssbscribers model
    """

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: Subscriber(r), self.collection)

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
        :return: Subscribers
        """
        if params is None:
            params = {}

        request = naas.requests.Subscribers.list(params)

        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
        else:
            Configuration.logger.error(
                "Failure retrieving the subscribers {request.status_code}"
            )
        return cls(klass_attributes)

    @staticmethod
    def retrieve(_id, params=None):
        """
        Helper method to retrieve from the request
        :param _id: str
        :param params: dict
        :return: Subscriber
        """
        if params is None:
            params = {}

        request = naas.requests.Subscribers.retrieve(_id, params)

        if request:
            return Subscriber(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {_id}")
            return

        Configuration.logger.error(
            "Failure retrieving the subscribern {request.status_code}"
        )

    @staticmethod
    def create(params=None):
        """
        Create a new subscriber
        :param params: dict
        :return: Subscriber
        """
        if params is None:
            params = {}

        request = naas.requests.Subscribers.create(params)

        if request:
            return Subscriber(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages}")

        Configuration.logger.error(failure_message)
        raise InvalidRequestError(failure_message)
