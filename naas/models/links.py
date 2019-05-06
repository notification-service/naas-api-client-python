from naas.models.link import Link
from naas.errors import LinkNotFoundError


class Links(object):
    """

    Links
    ===============

    This returns an instance of the Links domain model
    """

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: Link(r), self.collection)

    def route_for(self, rel):
        """Returns the route for the link relationship"""
        return Link(
            next(filter(lambda r: Link(r).rel() == rel, self.collection)))

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    def find_by_rel(self, rel):
        """
        Find the link by its relationship
        :raises LinkNotFoundError
        :return: Link
        """
        for record in self.collection:
            if Link(record).rel() == rel:
                return record
        raise LinkNotFoundError
