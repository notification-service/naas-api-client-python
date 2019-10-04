import iso8601
from naas.models.links import Links


class DataType(object):
    """

    DataType
    ===============

    This returns an instance of the DataType domain model
    """

    def __init__(self, attributes={}):
        self.attributes = attributes

    def _id(self):
        """Returns the data type id"""
        return self.attributes.get('id')

    def name(self):
        """Returns the data type name"""
        return self.attributes.get('name')

    def description(self):
        """Returns the data type description"""
        return self.attributes.get('description')

    def created_at(self):
        """Returns the created at timestamp"""
        return iso8601.parse_date(self.attributes.get('created_at'))

    def updated_at(self):
        """Returns the updated at timestamp"""
        return iso8601.parse_date(self.attributes.get('updated_at'))

    def links_attributes(self):
        """Returns the links attributes"""
        return self.attributes.get('links', [])

    def links(self):
        return Links(self.links_attributes())

    def to_a(self):
        """Returns the record serialized as an array"""
        return [self._id(), self.name(), self.description(), self.created_at()]

    def to_option(self):
        """Returns the record as an option"""
        return [self.name(), self._id()]
