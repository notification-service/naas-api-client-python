from naas.requests.email_notification_statuses import EmailNotificationStatuses
from tests import BaseTestCase


class TestRequestsEmailNotificationStatuses(BaseTestCase):

    def test_retrieve_by_email_notification_id(self):
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
        response = EmailNotificationStatuses.retrieve_by_email_notification_id(
            email_notification.json()['data']['id'])
        self.assertEqual(response.status_code, 200)

    def test_retrieve_by_email_notification_invalid_id_unsuccessful(self):
        response = EmailNotificationStatuses.retrieve_by_email_notification_id(
            "invalid_id")
        self.assertEqual(response.status_code, 404)
