from naas.requests.accounts import Accounts
from tests import BaseTestCase


class TestRequestsAccounts(BaseTestCase):

    def test_retrieve(self):
        response = Accounts.retrieve()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_update(self):
        name = "Python Client"
        response = Accounts.update({"name": name})
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['data']['name'], name)
