import iso8601
from naas.models.links import Links
from naas.models.project import Project
from naas.models.projects import Projects
from naas.models.project_property import ProjectProperty
from naas.models.project_properties import ProjectProperties
from naas.models.project_subscriber import ProjectSubscriber
from nnaas.models.project_subscribers import ProjectSubscribers


class ProjectSubscriberProperty(object):
    """

     ProjectSubscriberProperty
    ===============

    This returns an instance of the  Project Subscriber Property domain model
    """

    def __init__(self, attributes={}):
        self.attributes = attributes

    def _id(self):
        """Returns the data type id"""
        return self.attributes.get('id')

    def project_id(self):
        """Returns the associated project id"""
        return self.attributes.get('project_id')

    def project_attributes(self):
        """Returns the project attributes"""
        return self.attributes.get('project', {})

    def project(self):
        """Returns an instance of the project"""
        if self.project_attributes():
            return Project(self.project_attributes())
        return Projects.retrieve(self.project_id())

    def project_property_id(self):
        """Returns the project property id"""
        return self.attributes.get('project_property_id')

    def project_property_attributes(self):
        """Returns the project property attributes"""
        return self.attributes.get('project_property', {})

    def project_property(self):
        """Returns an instance of the project property"""
        if self.project_property_attributes():
            return ProjectProperty(self.project_property_attributes())
        return ProjectProperties.retrieve_by_project_id(
            self.project_id(), self.project_property_id())

    def project_subscriber_id(self):
        """Returns the project subscriber id"""
        return self.attributes.get('project_subscriber_id')

    def project_subscriber_attributes(self):
        """Returns the project subscriber attributes"""
        return self.attributes.get('project_subscriber', {})

    def project_subscriber(self):
        """Returns an instance of the project subscriber"""
        if self.project_subscriber_attributes():
            return ProjectSubscriber(self.project_subscriber_attributes())
        return ProjectSubscribers.retrieve_by_project_id(
            self.project_id(), self.project_subscriber_id())

    def value_before_typecast(self):
        """This is the raw value before typecase"""
        return self.attributes.get('value')

    def value(self):
        return self.value_before_typecast()

    def is_subscriber_editable(self):
        return self.attributes.get('is_subscriber_editable')

    def created_at(self):
        """Returns the created at timestamp value"""
        return iso8601.parse_date(self.attributes.get('created_at'))

    def updated_at(self):
        """Returns the updated at timestamp value"""
        return iso8601.parse_date(self.attributes.get('updated_at'))

    def links_attributes(self):
        """Returns the links attributes"""
        return self.attributes.get('links', [])

    def links(self):
        """Returns links"""
        return Links(self.links_attributes())
