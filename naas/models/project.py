"""

Project
===============

This returns an instance of the Project domain model
"""
class Project(object):
    def __init__(self, attributes):
        self.attributes = attributes

    def id(self):
        """Returns the project id"""
        return self.attributes.get('id', None)

    def name(self):
        """Returns the project name"""
        return self.attributes.get('name', None)

    def description(self):
        """Returns the description"""
        return self.attributes.get('description', None)

    def created_at_value(self):
        """Returns the created at timestamp value"""
        return self.attributes.get('created_at', None)

    def created_at(self):
        """Returns the created at timestamp"""
        date_format = '%Y-%m-%dT%H:%M:%S%z'
        date_value  = self.created_at_value

        try:
            return datetime.datetime.strptime(date_value, date_format)
        except ValueError as e:
            return None

    def updated_at_value(self):
        """Returns the updated at timestamp value"""
        return self.attributes.get('updated_at', None)

    def links_attributes(self):
        """Returns the links collection attributes"""
        return self.attributes.get('links', [])
