from naas.requests.campaigns import Campaigns
from naas.requests.campaign_email_templates import CampaignEmailTemplates
from naas.requests.projects import Projects
from tests import BaseTestCase


class TestRequestsCampaignEmailTemplates(BaseTestCase):

    def test_create_by_invalid_project_id_and_invalid_campaign_id_fail(self):
        campaign_email_template_attributes = {
            "id": 'test_template',
            "name": 'Testing Email Templates',
            "subject": 'Hi there, this is a test',
            "from_email_address": 'test@testing.com',
            "from_name": 'Campaign Tester',
            "text_body": 'Thank you for subscribing to our app!',
            "html_body": '<h1>Welcome awesome user to this Application!</h1>'
        }
        response = CampaignEmailTemplates.create_by_project_id_and_campaign_id(
            'invalid_proj',
            'invalid_camp',
            campaign_email_template_attributes
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'Not Found')

    def test_create_by_valid_project_id_and_invalid_campaign_id_fail(self):
        campaign_email_template_attributes = {
            "id": 'test_template',
            "name": 'Testing Email Templates',
            "subject": 'Hi there, this is a test',
            "from_email_address": 'test@testing.com',
            "from_name": 'Campaign Tester',
            "text_body": 'Thank you for subscribing to our app!',
            "html_body": '<h1>Welcome awesome user to this Application!</h1>'
        }
        params_project = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        response_project = Projects.create(params_project)
        project_created = response_project.json()['data']

        response = CampaignEmailTemplates.create_by_project_id_and_campaign_id(
            project_created['id'],
            'invalid_camp',
            campaign_email_template_attributes
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'Not Found')

    def test_create_by_project_id_and_campaign_id_no_params_fail(self):
        params_project = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        response_project = Projects.create(params_project)
        project_created = response_project.json()['data']

        params_campaign = {'name': 'testing', 'description': 'My description'}
        response_campaign = Campaigns.create_by_project_id(
            project_created['id'], params_campaign)
        campaign_created = response_campaign.json()['data']

        response = CampaignEmailTemplates.create_by_project_id_and_campaign_id(
            project_created['id'],
            campaign_created['id']
        )
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], 'Bad Request')
        self.assertEqual(
            response.json()['errors'],
            ['param is missing or the value is empty: campaign_email_template']
        )

    def test_create_by_project_id_and_campaign_id_with_params_successful(self):
        campaign_email_template_attributes = {
            "id": 'test_template',
            "name": 'Testing Email Templates',
            "subject": 'Hi there, this is a test',
            "from_email_address": 'test@testing.com',
            "from_name": 'Campaign Tester',
            "text_body": 'Thank you for subscribing to our app!',
            "html_body": '<h1>Welcome awesome user to this Application!</h1>'
        }
        params_project = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        response_project = Projects.create(params_project)
        project_created = response_project.json()['data']

        params_campaign = {'name': 'testing', 'description': 'My description'}
        response_campaign = Campaigns.create_by_project_id(
            project_created['id'], params_campaign)
        campaign_created = response_campaign.json()['data']

        response = CampaignEmailTemplates.create_by_project_id_and_campaign_id(
            project_created['id'],
            campaign_created['id'],
            campaign_email_template_attributes
        )
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['data']['campaign_id'],
                         campaign_created['id'])
        self.assertEqual(response.json()['data']['id'],
                         campaign_email_template_attributes['id'])

    def test_list_by_project_id_and_campaign_id_invalid_id_unsuccessful(self):
        response = CampaignEmailTemplates.list_by_project_id_and_campaign_id(
            'invalid_proj',
            'invalid_camp'
        )
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'Not Found')

    def test_list_by_project_id_and_campaign_id_valid_id_successful(self):
        params_project = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        response_project = Projects.create(params_project)
        project_created = response_project.json()['data']

        params_campaign = {'name': 'testing', 'description': 'My description'}
        response_campaign = Campaigns.create_by_project_id(
            project_created['id'], params_campaign)
        campaign_created = response_campaign.json()['data']
        response = CampaignEmailTemplates.list_by_project_id_and_campaign_id(
            project_created['id'],
            campaign_created['id']
        )
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json()['data'], list)

    def test_retrieve_by_project_id_and_campaign_id_invalid_id_fail(self):
        resp = CampaignEmailTemplates.retrieve_by_project_id_and_campaign_id(
            'invalid_proj',
            'invalid_camp',
            'invalid_template'
        )
        self.assertEqual(resp.status_code, 404)
        self.assertEqual(resp.json()['message'], 'Not Found')

    def test_retrieve_by_project_id_and_campaign_id_valid_id_successful(self):
        campaign_email_template_attributes = {
            "id": 'test_template',
            "name": 'Testing Email Templates',
            "subject": 'Hi there, this is a test',
            "from_email_address": 'test@testing.com',
            "from_name": 'Campaign Tester',
            "text_body": 'Thank you for subscribing to our app!',
            "html_body": '<h1>Welcome awesome user to this Application!</h1>'
        }
        params_project = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        response_project = Projects.create(params_project)
        project_created = response_project.json()['data']

        params_campaign = {'name': 'testing', 'description': 'My description'}
        response_campaign = Campaigns.create_by_project_id(
            project_created['id'], params_campaign)
        campaign_created = response_campaign.json()['data']

        email_tp = CampaignEmailTemplates.create_by_project_id_and_campaign_id(
            project_created['id'],
            campaign_created['id'],
            campaign_email_template_attributes
        )
        email_template_created = email_tp.json()['data']
        resp = CampaignEmailTemplates.retrieve_by_project_id_and_campaign_id(
            project_created['id'],
            campaign_created['id'],
            email_template_created['id']
        )
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.json()['data']['id'],
                         campaign_email_template_attributes['id'])
        self.assertEqual(resp.json()['data']['campaign_id'],
                         campaign_created['id'])
