from naas.requests.campaigns import Campaigns
from naas.requests.projects import Projects
from tests import BaseTestCase


class TestRequestsCampaigns(BaseTestCase):

    def test_create_by_project_id_no_params_unsuccessful(self):
        response = Campaigns.create_by_project_id("random_id")
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], 'Bad Request')
        self.assertEqual(response.json()['errors'],
                         ['param is missing or the value is empty: campaign'])

    def test_create_by_project_id_invalid_id_unsuccessful(self):
        params = {'name': 'testing', 'description': 'My description'}
        response = Campaigns.create_by_project_id("random_id", params)
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'Not Found')

    def test_create_by_project_id_valid_id_missing_name_unsuccessful(self):
        params_project = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        params_campaign = {'description': 'My description'}
        response_project = Projects.create(params_project)
        project_created = response_project.json()['data']
        response = Campaigns.create_by_project_id(
            project_created['id'], params_campaign)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json()['data']['message'], 'Conflict')
        self.assertEqual(response.json()['data']['errors'][0]['message'],
                         "Name can't be blank")

    def test_create_by_project_id_valid_id_with_params_successful(self):
        params_project = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        params_campaign = {'name': 'testing', 'description': 'My description'}
        response_project = Projects.create(params_project)
        project_created = response_project.json()['data']
        response = Campaigns.create_by_project_id(
            project_created['id'], params_campaign)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['data']['project_id'],
                         project_created['id'])
        self.assertEqual(response.json()['data']['name'],
                         params_campaign['name'])

    def test_list_by_project_id_invalid_id_unsuccessful(self):
        response = Campaigns.list_by_project_id("invalid_id")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'Not Found')

    def test_list_by_project_id_valid_id_successful(self):
        params_project = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        params_campaign = {'name': 'testing', 'description': 'My description'}
        response_project = Projects.create(params_project)
        project_created = response_project.json()['data']
        response_campaign = Campaigns.create_by_project_id(
            project_created['id'], params_campaign)
        response = Campaigns.list_by_project_id(project_created['id'])
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json()['data'], list)
        self.assertEqual(response.json()['data'][0]['name'],
                         params_campaign['name'])
        self.assertEqual(response.json()['data'][0]['name'],
                         response_campaign.json()['data']['name'])

    def test_retrieve_by_project_id_invalid_project_id_invalid_id_fails(self):
        response = Campaigns.retrieve_by_project_id(
            "invalid_project_id", "invalid_campaign_id")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'Not Found')

    def test_retrieve_by_project_id_valid_project_id_invalid_id_fails(self):
        params_project = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        response_project = Projects.create(params_project)
        project_created = response_project.json()['data']

        response = Campaigns.retrieve_by_project_id(
            project_created['id'], "invalid_campaign_id")
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'Not Found')

    def test_retrieve_by_project_id_successful(self):
        params_project = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        params_campaign = {'name': 'testing', 'description': 'My description'}
        response_project = Projects.create(params_project)
        project_created = response_project.json()['data']
        response_campaign = Campaigns.create_by_project_id(
            project_created['id'], params_campaign)
        campaign_created = response_campaign.json()['data']
        response = Campaigns.retrieve_by_project_id(
            project_created['id'], campaign_created['id'])
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['name'],
                         params_campaign['name'])
