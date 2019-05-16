from naas.requests.projects import Projects
from tests import BaseTestCase


class TestRequestsProjects(BaseTestCase):

    def test_list(self):
        response = Projects.list()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_create_no_params_unsuccessful(self):
        response = Projects.create()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], 'Bad Request')
        self.assertEqual(response.json()['errors'],
                         ['param is missing or the value is empty: project'])

    def test_create_missing_name_parameter_unsuccessful(self):
        params = {'description': 'Test description'}
        response = Projects.create(params)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json()['data']['message'], 'Conflict')
        self.assertEqual(response.json()['data']['errors'][0]['message'],
                         "Name can't be blank")

    def test_create_with_params_successful(self):
        params = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        response = Projects.create(params)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['data']['name'], params['name'])

    def test_retrieve_invalid_id_unsuccessful(self):
        response = Projects.retrieve('invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'Not Found')

    def test_retrieve_valid_id_successful(self):
        params = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        response_create = Projects.create(params)
        project_created = response_create.json()['data']

        response_retrieve = Projects.retrieve(project_created['id'])
        self.assertEqual(response_retrieve.status_code, 200)
        self.assertEqual(response_retrieve.json()['data']['name'],
                         params['name'])

    def test_update_invalid_id_unsuccessful(self):
        response = Projects.update('invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'Not Found')

    def test_update_valid_id_no_params_unsuccessful(self):
        params = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        response_create = Projects.create(params)
        project_created = response_create.json()['data']

        response = Projects.update(project_created['id'])
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], 'Bad Request')
        self.assertEqual(response.json()['errors'],
                         ['param is missing or the value is empty: project'])

    def test_update_valid_id_params_successful(self):
        params = {
            'name': 'My Initial Project',
            'description': 'My initial description'
        }
        response_create = Projects.create(params)
        project_created = response_create.json()['data']

        updated_params = {'name': 'Updated Name'}
        response = Projects.update(project_created['id'], updated_params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['id'], project_created['id'])
        self.assertEqual(response.json()['data']['name'],
                         updated_params['name'])
        self.assertNotEqual(response.json()['data']['name'], params['name'])
