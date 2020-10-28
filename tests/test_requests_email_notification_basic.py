from naas.requests.email_notification_basics import EmailNotificationBasics
from tests import BaseTestCase


class TestRequestsEmailNotificationBasics(BaseTestCase):

    def test_create_no_params_unsuccessful(self):
        response = EmailNotificationBasics.create()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['data']['message'], 'Bad Request')
        self.assertEqual(
            response.json()['data']['errors'][0]['message'],
            'param is missing or the value is empty: email_notification_basic'
        )

    def test_create_successful(self):
        project_id = self.create_project().json()['data']['id']
        campaign_id = self.create_campaign(project_id).json()['data']['id']
        campaign_email_tempalate_id = self.create_campaign_email_template(
            project_id, campaign_id
        ).json()['data']['id']
        response = EmailNotificationBasics.create_from_attributes(
            f'test{project_id}@gmail.com', project_id, campaign_id,
            campaign_email_tempalate_id
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.json()['data']['campaign_email_template_id'],
            campaign_email_tempalate_id
        )
