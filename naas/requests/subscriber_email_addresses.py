import json
from naas.client import Client


class SubscriberEmailAddresses:

    @staticmethod
    def list(params=None):
        """
        Retrieve the list of subscriber email addresses

        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/subscriber-email-addresses')
        route = Client.routes().route_for(rel)
        url = route.url_for(params)
        request = Client.get(url)
        return request

    @staticmethod
    def retrieve(_id, params=None):
        """
        Retrieve the instance of a subscriber email address

        :param _id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/subscriber-email-address')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'id': _id}})
        request = Client.get(url)
        return request

    @staticmethod
    def create(params=None):
        """
        Created a new record

        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        request_body = {
            "subscriber_email_address": params
        }
        request_headers = {
            "Content-Type": "application/json"
        }
        rel = Client.rel_for('rels/subscriber-email-addresses')
        route = Client.routes().route_for(rel)
        url = route.url_for()
        request = Client.post(
            url, headers=request_headers, data=json.dumps(request_body))
        return request

    @staticmethod
    def list_by_subscriber_id(subscriber_id, params=None):
        """
        Retrieve the list of the subscriber email addresses by subscriber

        :param subscriber_id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/subscriber-subscriber-email-addresses')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={
            **params, **{'subscriber_id': subscriber_id}
        })
        request = Client.get(url)
        return request
