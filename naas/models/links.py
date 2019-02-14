from naas.models.link import Link
"""

Links
===============

This returns an instance of the Links domain model
"""
class Links(object):
    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: Link(r), self.collection)

    def route_for(self, rel):
        """Returns the route for the link relationship"""
        return next(filter(lambda r: r.rel() == rel, self))

    def next(self):
        if self.index == 0:
          raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]