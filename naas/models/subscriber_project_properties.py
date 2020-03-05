from naas.models.subscriber_project_property import SubscriberProjectProperty


class SubscriberProjectProperties(object):
    """

    Subscriber Project Properties
    ===============

    This returns an instance of the subscriber project properties
    """

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: SubscriberProjectProperty(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]
