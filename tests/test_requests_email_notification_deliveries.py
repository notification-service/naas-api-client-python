from naas.requests.email_notification_deliveries import EmailNotificationDeliveries
from tests import BaseTestCase


class TestRequestsEmailNotificationDeliveries(BaseTestCase):

    def email_notification(self):
        account_smtp_setting_id = self.create_smtp_Settings().json()[
            'data']['id']
        project_id = self.create_project().json()['data']['id']
        campaign_id = self.create_campaign(project_id).json()['data']['id']
        email_template_id = self.create_campaign_email_template(
            project_id, campaign_id).json()['data']['id']
        subscriber_email_id = self.create_subscriber_email_address().json()[
            'data']['id']
        return self.create_email_notification(
            account_smtp_setting_id, email_template_id, subscriber_email_id)

    def test_list_by_email_notification_id(self):
        response = EmailNotificationDeliveries.list_by_email_notification_id(
            self.email_notification().json()['data']['id'])
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
