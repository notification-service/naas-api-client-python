from naas.requests.account_settings import AccountSettings
from tests import BaseTestCase


class TestRequestsAccountSettings(BaseTestCase):

    def test_retrieve(self):
        response = AccountSettings.retrieve()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_disable_send_grid(self):
        response = AccountSettings.disable_send_grid()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
        self.assertIsNone(response.json()['data']['send_grid_webhook_token'])
        self.assertIsNone(response.json()['data']['send_grid_webhook_url'])

    def test_enable_send_grid_when_disabled_successful(self):
        AccountSettings.disable_send_grid()
        response = AccountSettings.enable_send_grid()
        self.assertEqual(response.status_code, 200)
        self.assertIsNotNone(
            response.json()['data']['send_grid_webhook_token'])
        self.assertIsNotNone(response.json()['data']['send_grid_webhook_url'])

    def test_enable_send_grid_when_already_enabled_unsuccessful(self):
        AccountSettings.disable_send_grid()
        AccountSettings.enable_send_grid()
        response = AccountSettings.enable_send_grid()
        self.assertEqual(response.status_code, 409)
        self.assertEqual(response.json()['data']['message'], 'Conflict')
        self.assertEqual(response.json()['data']['errors'][0]['message'],
                         'SendGrid is already enabled')
