from naas.models.project import Project


class Projects(object):
    def __init__(self, collection):
        self.collection = list(collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: Project(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]
