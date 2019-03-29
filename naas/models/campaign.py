"""

Campaign
===============

This returns an instance of the Campaign domain model
"""
from naas.models import Links, CampaignEmailTemplates


class Campaign(object):
    def __init__(self, attributes={}):
        self.attributes = attributes

    def id(self):
        """Returns the id"""
        return self.attributes.get('id')

    def project_id(self):
        """Returns the id"""
        return self.attributes.get('project_id')

    def name(self):
        """Returns the name"""
        return self.attributes.get('name')

    def description(self):
        """Returns the description"""
        return self.attributes.get('description')

    def campaign_email_templates_attributes(self):
        """Return the associated campaign email templates"""
        return self.attributes.get('campaign_email_templates', [])

    def campaign_email_templates(self):
        if self.campaign_email_templates_attributes():
            return CampaignEmailTemplates(
                self.campaign_email_templates_attributes())
        else:
            return CampaignEmailTemplates.list_by_project_id_and_campaign_id(
                self.project_id(), self.id())

    def created_at(self):
        """Returns the created at timestamp value"""
        return self.attributes.get('created_at')

    def updated_at(self):
        """Returns the updated at timestamp value"""
        return self.attributes.get('updated_at')

    def links_attributes(self):
        """Returns the links collection attributes"""
        return self.attributes.get('links', [])

    def links(self):
        """Returns links"""
        return Links(self.links_attributes())
