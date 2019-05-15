import os
import unittest
import json
from naas.configuration import Configuration
from naas.requests.account_smtp_settings import AccountSmtpSettings
from naas.requests.campaigns import Campaigns
from naas.requests.campaign_email_templates import CampaignEmailTemplates
from naas.requests.email_notifications import EmailNotifications
from naas.requests.projects import Projects
from naas.requests.subscribers import Subscriber
from naas.requests.subscriber_email_addresses import SubscriberEmailAddresses


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        config = Configuration()
        config.access_token = os.getenv("NAAS_ACCESS_TOKEN_TEST")
        config.api_host = os.getenv("NAAS_API_HOST_TEST")

    def tearDown(self):
        pass

    @staticmethod
    def create_smtp_Settings():
        attributes = {
            "port": os.getenv("TEST_PORT"),
            "authentication_type_value": "plain",
            "is_primary": True,
            "name": "Gmail",
            "address": "smtp.gmail.com",
            "password_confirmation": os.getenv("TEST_PASSWORD"),
            "password": os.getenv("TEST_PASSWORD"),
            "user_name": os.getenv("TEST_EMAIL"),
            "description": "Test domain account",
            "domain": "gmail.com"
        }
        return AccountSmtpSettings.create(attributes)

    @staticmethod
    def create_campaign_email_template(project_id, campaign_id):
        attributes = {
            "id": 'test_template',
            "name": 'Testing Email Templates',
            "subject": 'Hi there, this is a test',
            "from_email_address": 'test@testing.com',
            "from_name": 'Campaign Tester',
            "text_body": 'Thank you for subscribing to our app!',
            "html_body": '<h1>Welcome awesome user to this Application!</h1>'
        }
        return CampaignEmailTemplates.create_by_project_id_and_campaign_id(
            project_id, campaign_id, attributes)

    @staticmethod
    def create_campaign(project_id):
        attributes = {'name': 'testing', 'description': 'My description'}
        return Campaigns.create_by_project_id(project_id, attributes)

    @staticmethod
    def create_project():
        attributes = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        return Projects.create(attributes)

    @staticmethod
    def create_subscriber():
        attributes = {
            'first_name': 'John',
            'last_name': 'Doe'
        }
        return Subscriber.create(attributes)

    def create_subscriber_email_address(self):
        subscriber_created = self.create_subscriber().json()['data']
        attributes = {
            "subscriber_id": subscriber_created["id"],
            "email_address": f'john_doe{subscriber_created["id"]}@gmail.com',
            "is_primary": True
        }
        return SubscriberEmailAddresses.create(attributes)

    @staticmethod
    def create_email_notification(
        account_smtp_setting_id, campaign_email_template_id,
        subscriber_email_address_id, content=None
    ):
        if not content:
            content = {}

        attributes = {
            "account_smtp_setting_id": account_smtp_setting_id,
            "campaign_email_template_id": campaign_email_template_id,
            "subscriber_email_address_id": subscriber_email_address_id,
            "content": content
        }
        return EmailNotifications.create(attributes)
