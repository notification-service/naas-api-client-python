from naas.requests.account_smtp_settings import AccountSmtpSettings
from tests import BaseTestCase
from naas.errors import RecordNotFoundError


class TestRequestsAccountSmtpSettings(BaseTestCase):

    def test_list(self):
        response = AccountSmtpSettings.list()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_create_no_params_unsuccessful(self):
        response = AccountSmtpSettings.create()
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.json()['message'], 'Bad Request')
        self.assertEqual(
            response.json()['errors'],
            ['param is missing or the value is empty: smtp_settings']
        )

    def test_create_successful(self):
        response = self.create_smtp_Settings()
        self.assertEqual(response.status_code, 201)

    def test_retrieve(self):
        create_setting = self.create_smtp_Settings()
        smtp_id = create_setting.json()['data']['id']
        response = AccountSmtpSettings.retrieve(smtp_id)
        self.assertEqual(response.status_code, 200)

    def test_retrieve_invalid_id_unsuccessful(self):
        with self.assertRaises(RecordNotFoundError):
            AccountSmtpSettings.retrieve("invalid_id")
