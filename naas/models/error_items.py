from naas.models.error_item import ErrorItem


class ErrorItems(object):
    """

    Error Items
    ===============

    This returns an instance of the error items model
    """

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: ErrorItem(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    def full_messages(self):
        """
        Returns the full messages as a string
        """
        return ', '.join(
            [ErrorItem(record).full_message() for record in self.collection])
