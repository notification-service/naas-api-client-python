import json
from naas.client import Client


class Subscriber:

    @classmethod
    def list(cls, params=None):
        """
        Retrieve the list of subscribers

        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/subscribers')
        route = Client.routes().route_for(rel)
        url = route.url_for(params)
        request = Client.get(url)
        return request

    @classmethod
    def retrieve(cls, _id, params=None):
        """
        Retrieve the instance of a subscriber

        :param _id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/subscriber')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'id': _id}})
        request = Client.get(url)
        return request

    @classmethod
    def create(cls, params=None):
        """
        Create a new subscriber

        :param params: dict Attributes for the domain model
        :return: Response
        """
        if params is None:
            params = {}
        request_body = {
            "subscriber": params
        }
        headers = {
            'Content-Type': 'application/json'
        }
        rel = Client.rel_for('rels/subscribers')
        route = Client.routes().route_for(rel)
        url = route.url_for()
        request = Client.post(
            url, headers=headers, data=json.dumps(request_body))
        return request

    @classmethod
    def update(cls, _id, params=None):
        """
        Update an existing subscriber

        :param _id: int
        :param params: dict Attributes for the domain model
        :return: Response
        """
        if params is None:
            params = {}
        request_body = {
            "subscriber": params
        }
        headers = {
            'Content-Type': 'application/json'
        }
        rel = Client.rel_for('rels/subscriber')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'id': _id}})
        request = Client.put(
            url, headers=headers, data=json.dumps(request_body))
        return request
