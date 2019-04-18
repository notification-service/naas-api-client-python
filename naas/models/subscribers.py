from nass.configuration import Configuration
from naas.errors import InvalidRequestError, RecordNotFoundError
from nass.models import Subscriber, Error
from naas.requests import Subscribers


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
        if params is None:
            params = {}

        request = Subscribers.list(params)

        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
        else:
            Configuration.logger.error(
                "Failure retrieving the subscribers {request.status_code}"
            )
        return cls(klass_attributes)

    @staticmethod
    def retrieve(id, params=None):
        if params is None:
            params = {}

        request = Subscribers.retrieve(id, params)

        if request:
            return Subscriber(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {id}")
            return

        Configuration.logger.error(
            "Failure retrieving the subscriber {request.status_code}"
        )

    @staticmethod
    def create(params=None):
        if params is None:
            params = {}

        request = Subscribers.create(params)

        if request:
            return Subscriber(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages}")

        Configuration.logger.error(failure_message)
        raise InvalidRequestError(failure_message)
