import os
import unittest
from naas.configuration import Configuration


class BaseTestCase(unittest.TestCase):

    def setUp(self):
        config = Configuration()
        config.access_token = os.getenv("NAAS_ACCESS_TOKEN_TEST")
        config.api_host = os.getenv("NAAS_API_HOST_TEST")

    def tearDown(self):
        pass
