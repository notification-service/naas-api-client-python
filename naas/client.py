import os
import requests


class Client(object):
    """

    naas.client
    ===============

    This module contains the helper methods to manage
    API requests.
    """

    @classmethod
    def default_headers(cls):
        """Returns the default headers for the requests"""
        headers = {
           'Authorization': f"Bearer {Client.access_token()}",
           'Accept': Client.default_accept_header()
        }
        return headers

    @classmethod
    def api_host(cls):
        """Returns the API Host"""
        api_host = os.environ['NAAS_API_HOST']
        return api_host

    @classmethod
    def access_token(cls):
        """Returns the Access Token"""
        access_token = os.environ['NAAS_ACCESS_TOKEN']
        return access_token

    @classmethod
    def default_accept_header(cls):
        header_value = 'application/vnd.naas.json; version=1'
        return header_value

    @classmethod
    def get(cls, url, headers=None, params=None):
        """Execute a GET request"""
        if headers is None:
            headers = {}
        if params is None:
            params = {}
        request_headers = {**Client.default_headers(), **headers}
        return requests.get(url, headers=request_headers, params=params)

    @classmethod
    def head(cls, url, headers=None, params=None):
        """Execute a HEAD request"""
        if headers is None:
            headers = {}
        if params is None:
            params = {}
        request_headers = {**Client.default_headers(), **headers}
        return requests.head(url, headers=request_headers, params=params)

    @classmethod
    def post(cls, url, headers=None, json=None):
        if headers is None:
            headers = {}
        if json is None:
            json = {}
        request_headers = {**Client.default_headers(), **headers}
        return requests.post(url, headers=request_headers, json=json)

    @classmethod
    def put(cls, url, headers=None, json=None):
        if headers is None:
            headers = {}
        if json is None:
            json = {}
        request_headers = {**Client.default_headers(), **headers}
        return requests.put(url, headers=request_headers, json=json)

    @classmethod
    def create_route(cls, endpoint):
        """Create routes from an endpoint"""
        return f"{Client.api_host()}/{endpoint}"
