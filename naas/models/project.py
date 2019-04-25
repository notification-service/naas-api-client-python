import iso8601

from naas.models import Links


class Project(object):
    """

    Project
    ===============

    This returns an instance of the Project domain model
    """

    def __init__(self, attributes):
        self.attributes = attributes

    def id(self):
        """Returns the project id"""
        return self.attributes.get('id')

    def name(self):
        """Returns the project name"""
        return self.attributes.get('name')

    def description(self):
        """Returns the description"""
        return self.attributes.get('description')

    def created_at_value(self):
        """Returns the created at timestamp value"""
        return self.attributes.get('created_at')

    def created_at(self):
        """Returns the created at timestamp"""
        date_value = self.created_at_value
        try:
            return iso8601.parse_date(date_value)
        except ValueError as e:
            return None

    def updated_at_value(self):
        """Returns the updated at timestamp value"""
        return self.attributes.get('updated_at')

    def links_attributes(self):
        """Returns the links collection attributes"""
        return self.attributes.get('links', [])

    def links(self):
        """Returns links"""
        return Links(self.links_attributes())
