import json
from naas.requests.email_notifications import EmailNotifications
from tests import BaseTestCase


class TestRequestsEmailNotifications(BaseTestCase):

    def test_list(self):
        response = EmailNotifications.list()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_create_no_params_unsuccessful(self):
        response = EmailNotifications.create()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['data']['message'], 'Bad Request')
        self.assertEqual(
            response.json()['data']['errors'][0]['message'],
            'param is missing or the value is empty: email_notification'
        )

    def test_create_successful(self):
        account_smtp_setting_id = self.create_smtp_Settings().json()[
            'data']['id']
        project_id = self.create_project().json()['data']['id']
        campaign_id = self.create_campaign(project_id).json()['data']['id']
        email_template_id = self.create_campaign_email_template(
            project_id, campaign_id).json()['data']['id']
        subscriber_email_id = self.create_subscriber_email_address().json()[
            'data']['id']
        response = self.create_email_notification(
            account_smtp_setting_id, email_template_id, subscriber_email_id
        )
        self.assertEqual(response.status_code, 201)

    def test_retrieve(self):
        account_smtp_setting_id = self.create_smtp_Settings().json()[
            'data']['id']
        project_id = self.create_project().json()['data']['id']
        campaign_id = self.create_campaign(project_id).json()['data']['id']
        email_template_id = self.create_campaign_email_template(
            project_id, campaign_id).json()['data']['id']
        subscriber_email_id = self.create_subscriber_email_address().json()[
            'data']['id']
        email_notification = self.create_email_notification(
            account_smtp_setting_id, email_template_id, subscriber_email_id
        )
        response = EmailNotifications.retrieve(
            email_notification.json()['data']['id'])
        self.assertEqual(response.status_code, 200)

    def test_preview_html(self):
        account_smtp_setting_id = self.create_smtp_Settings().json()[
            'data']['id']
        project_id = self.create_project().json()['data']['id']
        campaign_id = self.create_campaign(project_id).json()['data']['id']
        email_template_id = self.create_campaign_email_template(
            project_id, campaign_id).json()['data']['id']
        subscriber_email_id = self.create_subscriber_email_address().json()[
            'data']['id']
        email_notification = self.create_email_notification(
            account_smtp_setting_id, email_template_id, subscriber_email_id
        )
        response = EmailNotifications.preview_html(
            email_notification.json()['data']['id'])
        self.assertEqual(response.status_code, 200)

    def test_deliver(self):
        account_smtp_setting_id = self.create_smtp_Settings().json()[
            'data']['id']
        project_id = self.create_project().json()['data']['id']
        campaign_id = self.create_campaign(project_id).json()['data']['id']
        email_template_id = self.create_campaign_email_template(
            project_id, campaign_id).json()['data']['id']
        subscriber_email_id = self.create_subscriber_email_address().json()[
            'data']['id']
        email_notification = self.create_email_notification(
            account_smtp_setting_id, email_template_id, subscriber_email_id
        )
        response = EmailNotifications.deliver(
            email_notification.json()['data']['id'])
        self.assertEqual(response.status_code, 201)
