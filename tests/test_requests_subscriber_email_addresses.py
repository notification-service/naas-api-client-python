from naas.requests.subscribers import Subscriber
from naas.requests.subscriber_email_addresses import SubscriberEmailAddresses
from tests import BaseTestCase


class TestRequestsSubscriberEmailAddresses(BaseTestCase):

    def test_list(self):
        response = SubscriberEmailAddresses.list()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_create_no_params_unsuccessful(self):
        response = SubscriberEmailAddresses.create()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], 'Bad Request')
        self.assertEqual(
            response.json()['errors'],
            ['param is missing or the value is empty: '
             'subscriber_email_address']
        )

    def test_create_with_invalid_subscriber_unsuccessful(self):
        subscriber_email_address_attributes = {
            "subscriber_id": "invalid",
            "email_address": 'jane_does@gmail.com',
            "is_primary": True
        }
        response = SubscriberEmailAddresses.create(
            subscriber_email_address_attributes)
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json()['data']['message'], 'Conflict')
        self.assertEqual(
            response.json()['data']['errors'][0]['message'],
            'Subscriber must exist'
        )

    def test_create_with_params_successful(self):
        subscriber = {
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response_subscriber = Subscriber.create(subscriber)
        subscriber_created = response_subscriber.json()['data']

        subscriber_email_address_attributes = {
            "subscriber_id": subscriber_created['id'],
            "email_address": f'john_doe{subscriber_created["id"]}@gmail.com',
            "is_primary": True
        }
        response = SubscriberEmailAddresses.create(
            subscriber_email_address_attributes)

        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()['data']['email_address'],
                         subscriber_email_address_attributes['email_address'])
        self.assertEqual(response.json()['data']['subscriber_id'],
                         subscriber_created['id'])

    def test_retrieve_invalid_id_unsuccessful(self):
        response = SubscriberEmailAddresses.retrieve('invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'Not Found')

    def test_retrieve_valid_id_successful(self):
        subscriber = {
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response_subscriber = Subscriber.create(subscriber)
        subscriber_created = response_subscriber.json()['data']

        subscriber_email_address_attributes = {
            "subscriber_id": subscriber_created['id'],
            "email_address": f'john_doe{subscriber_created["id"]}@gmail.com',
            "is_primary": True
        }
        response_subscriber_email = SubscriberEmailAddresses.create(
            subscriber_email_address_attributes)

        response_retrieve = SubscriberEmailAddresses.retrieve(
            response_subscriber_email.json()['data']['id'])

        self.assertEqual(response_retrieve.status_code, 200)

        self.assertEqual(response_retrieve.json()['data']['subscriber_id'],
                         subscriber_created['id'])

    def test_list_by_subscriber_id_invalid_id_unsuccessful(self):
        response = SubscriberEmailAddresses.list_by_subscriber_id('invalid_id')
        self.assertEqual(response.status_code, 404)
        self.assertEqual(response.json()['message'], 'Not Found')

    def test_list_by_subscriber_id_valid_id_successful(self):
        subscriber = {
            'first_name': 'John',
            'last_name': 'Doe'
        }
        response_subscriber = Subscriber.create(subscriber)
        subscriber_created = response_subscriber.json()['data']

        subscriber_email_address_attributes = {
            "subscriber_id": subscriber_created['id'],
            "email_address": f'john_doe{subscriber_created["id"]}@gmail.com',
            "is_primary": True
        }
        SubscriberEmailAddresses.create(
            subscriber_email_address_attributes)

        response_list = SubscriberEmailAddresses.list_by_subscriber_id(
            subscriber_created['id'])
        self.assertEqual(response_list.status_code, 200)
        self.assertIsInstance(response_list.json()['data'], list)
        self.assertEqual(response_list.json()['data'][0]['email_address'],
                         subscriber_email_address_attributes['email_address'])
