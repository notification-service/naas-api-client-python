"""

Campaign Email Template
===============

This returns an instance of the Campaign Email Template domain model
"""
from naas.models import Links


class CampaignEmailTemplate(object):
    def __init__(self, attributes={}):
        self.attributes = attributes

    def id(self):
        """Returns the id"""
        return self.attributes.get('id')

    def campaign_id(self):
        """Returns the campaign id"""
        return self.attributes.get('id')

    def name(self):
        """Returns the name"""
        return self.attributes.get('name')

    def description(self):
        """Returns the description"""
        return self.attributes.get('description')

    def subject(self):
        """Returns the subject template"""
        return self.attributes.get('subject')

    def from_email_address(self):
        """Returns the from email address"""
        return self.attributes.get('from_email_address')

    def from_name(self):
        """Returns the from name"""
        return self.attributes.get('from_name')

    def html_body(self):
        """Returns the html_body"""
        return self.attributes.get('html_body')

    def text_body(self):
        """Returns the text body"""
        return self.attributes.get('text_body')

    def created_at(self):
        """Returns the created at timestamp value"""
        return self.attributes.get('created_at')

    def updated_at(self):
        """Returns the updated at timestamp value"""
        return self.attributes.get('updated_at')

    def links_attributes(self):
        """Returns the links attributes"""
        return self.attributes.get('links', [])

    def links(self):
        return Links(self.links_attributes())
