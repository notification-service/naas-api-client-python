import os
import requests
from naas.models.directory import Directory


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
    def post(cls, url, headers=None, data=None, files=None):
        if headers is None:
            headers = {}
        if data is None:
            data = {}
        if files is None:
            files = {}
        request_headers = {**Client.default_headers(), **headers}
        return requests.post(
            url, headers=request_headers, files=files, data=data)

    @classmethod
    def put(cls, url, headers=None, data=None, files=None):
        if headers is None:
            headers = {}
        if data is None:
            data = {}
        if files is None:
            files = {}
        request_headers = {**Client.default_headers(), **headers}
        return requests.put(
            url, headers=request_headers, files=files, data=data)

    # TODO Define this
    # def configuration(self):
    #     return Configuration()

    @classmethod
    def directory(cls):
        """
        Returns the root directory response
        :return: naas.models.directory.Directory
        """
        return Directory.retrieve()

    @classmethod
    def routes(cls):
        """
        Define the API routes
        These are the endpoints that will be used to interact
        with the API. Before you make any requests you will
        want to add the corresponding routes here.

        :return: A collection of Routes
        """
        return cls.directory().links()

    @classmethod
    def rel_for(cls, rel):
        """
        Returns the link relationship for a specified path.
        Custom link relationships are fully qualified
        URIS, but in this case we only care to reference
        the path and add the API host.

        :return: String
        """
        return f'{cls.api_host()}/{rel}'
