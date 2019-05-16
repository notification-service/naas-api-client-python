import json
from naas.client import Client


class EmailNotifications:

    @staticmethod
    def list(params=None):
        """
        Retrieve the list of email notifications

        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/email-notifications')
        route = Client.routes().route_for(rel)
        url = route.url_for(params)
        request = Client.get(url)
        return request

    @staticmethod
    def retrieve(_id, params=None):
        """
        Retrieve the instance of a email notification

        :param _id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/email-notification')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'id': _id}})
        request = Client.get(url)
        return request

    @staticmethod
    def update(_id, params=None):
        """
        Update an existing record

        :param _id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        request_body = {
            "email_notification": params
        }
        request_headers = {
            "Content-Type": "application/json"
        }
        rel = Client.rel_for('rels/email-notification')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'id': _id}})
        request = Client.put(
            url, headers=request_headers, data=json.dumps(request_body))
        return request

    @staticmethod
    def create(params=None):
        """
        Create a new record

        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        request_body = {
            "email_notification": params
        }
        request_headers = {
            "Content-Type": "application/json"
        }
        rel = Client.rel_for('rels/email-notifications')
        route = Client.routes().route_for(rel)
        url = route.url_for()
        request = Client.post(
            url, headers=request_headers, data=json.dumps(request_body))
        return request

    @staticmethod
    def deliver(_id, params=None):
        """
        Deliver the instance of a email notification

        :param _id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/email-notification-deliver')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'id': _id}})
        request = Client.post(url)
        return request

    @staticmethod
    def preview_html(_id, params=None):
        """
        Preview the instance of a email notification

        :param _id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/email-notification-preview')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'id': _id}})
        request = Client.get(url)
        return request
