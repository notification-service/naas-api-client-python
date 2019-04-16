class JSONParseError(Exception):
    """
    Exception raised when there is an error parsing JSON
    """
    pass


class RecordNotFoundError(Exception):
    """
    Exception raised when a certain record is not found
    """
    pass


class LinkNotFoundError(Exception):
    """
    Exception raised when a certain link is not found
    """
    pass


class InvalidRequestError(Exception):
    """
    Exception raised where an invalid request is made
    """
    pass
