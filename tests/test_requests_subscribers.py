from naas.requests.subscribers import Subscriber
from tests import BaseTestCase


class TestRequestsSubscribers(BaseTestCase):

    def test_list(self):
        response = Subscriber.list()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_create_no_params_unsuccessful(self):
        response = Subscriber.create()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['data']['message'], 'Bad Request')
        self.assertEqual(
            response.json()['data']['errors'][0]['message'],
            'param is missing or the value is empty: subscriber'
        )

    def test_create_with_params_successful(self):
        subscriber = {
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response = Subscriber.create(subscriber)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['data']['first_name'],
                         subscriber['first_name'])
        self.assertEqual(response.json()['data']['last_name'],
                         subscriber['last_name'])

    def test_retrieve_invalid_id_unsuccessful(self):
        response = Subscriber.retrieve('invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['data']['message'], 'Not Found')

    def test_retrieve_valid_id_successful(self):
        subscriber = {
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response_create = Subscriber.create(subscriber)
        subscriber_created = response_create.json()['data']

        response_retrieve = Subscriber.retrieve(subscriber_created['id'])

        self.assertEqual(response_retrieve.status_code, 200)
        self.assertEqual(response_retrieve.json()['data']['first_name'],
                         subscriber['first_name'])

    def test_update_invalid_id_unsuccessful(self):
        response = Subscriber.update('invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['data']['message'], 'Not Found')

    def test_update_valid_id_no_params_unsuccessful(self):
        subscriber = {
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response_create = Subscriber.create(subscriber)
        subscriber_created = response_create.json()['data']

        response = Subscriber.update(subscriber_created['id'])

        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['data']['message'], 'Bad Request')
        self.assertEqual(
            response.json()['data']['errors'][0]['message'],
            'param is missing or the value is empty: subscriber'
        )

    def test_update_valid_id_params_successful(self):
        subscriber = {
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response_create = Subscriber.create(subscriber)
        subscriber_created = response_create.json()['data']

        updated_params = {'first_name': 'Jane'}

        response = Subscriber.update(subscriber_created['id'], updated_params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.json()['data']['id'],
            subscriber_created['id']
        )
        self.assertEqual(
            response.json()['data']['first_name'],
            updated_params['first_name']
        )
        self.assertNotEqual(
            response.json()['data']['first_name'],
            subscriber['first_name']
        )
