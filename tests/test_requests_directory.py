from naas.requests.directory import Directory
from tests import BaseTestCase


class TestRequestsDirectory(BaseTestCase):

    def test_retrieve(self):
        response = Directory.retrieve()
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
