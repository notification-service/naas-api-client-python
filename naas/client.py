"""

naas.client
===============

This module contains the helper methods to manage
API requests.
"""

import os
import requests

class Client(object):
    @classmethod
    def default_headers(cls):
        """Returns the default headers for the requests"""
        headers = {
           'Authorization': ("Bearer %s" %(Client.access_token())),
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
    def get(cls, url, headers={}, params={}):
        """Execute a GET request"""
        request_headers = { **Client.default_headers(), **headers }
        return requests.get(url, headers=request_headers)

    @classmethod
    def head(cls, url, headers={}, params={}):
        """Execute a HEAD request"""
        request_headers = { **Client.default_headers(), **headers }
        return requests.head(url, headers=request_headers)

    @classmethod
    def routes(cls):
        """Routes"""
        return Client.get(Client.api_host())
