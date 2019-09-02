import iso8601
from naas.models.data_type import DataType
from naas.models.data_types import DataTypes
from naas.models.links import Links


class ProjectProperty(object):
    """

    ProjectProperty
    ===============

    This returns an instance of the ProjectProperty domain model
    """

    def __init__(self, attributes={}):
        self.attributes = attributes

    def _id(self):
        """Returns the data type id"""
        return self.attributes.get('id')

    def project_id(self):
        """Returns the associated project id"""
        return self.attributes.get('project_id')

    def data_type_id(self):
        """Returns the associated project id"""
        return self.attributes.get('data_type_id')

    def data_type_attributes(self):
        """Returns the associated project id"""
        return self.attributes.get('data_type', {})

    def data_type(self):
        """Returns the data type model"""
        if self.data_type_attribute():
            return naas.models.DataType(self.data_type_attributes)
        return naas.models.DataTypes.retrieve(self.data_type_id())

    def name(self):
        """Returns the data type name"""
        return self.attributes.get('name')

    def key_name(self):
        """Returns the key name"""
        return self.attributes.get('key_name')

    def description(self):
        """Returns the data type description"""
        return self.attributes.get('description')

    def created_at(self):
        """Returns the created at timestamp"""
        return iso8601.parse_date(self.attributes.get('created_at'))

    def updated_at(self):
        """Returns the updated at timestamp"""
        return iso8601.parse_date(self.attributes.get('updated_at'))

    def is_subscriber_editable(self):
        """Returns true if is subscriber editable"""
        return self.attributes.get('is_subscriber_editable')

    def is_subscriber_viewable(self):
        """Returns true if is subscriber viewable"""
        return self.attributes.get('is_subscriber_viewable')

    def links_attributes(self):
        """Returns the links attributes"""
        return self.attributes.get('links', [])

    def links(self):
        return Links(self.links_attributes())

    def to_a(self):
        """Serialized the record as an array"""
        return [
            self._id(), self.project_id(), self.data_type_id(), self.name(),
            self.key_name(), self.description(), self.is_subscriber_editable(),
            self.is_subscriber_viewable(), self.created_at()
        ]
