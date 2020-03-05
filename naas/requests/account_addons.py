import json
from naas.client import Client


class AccountAddons:

    @staticmethod
    def list(params=None):
        """
        Retrieve the list of Account Addons

        :param params: dict
        :return: Response
        """
        rel   = Client.rel_for('rels/account-addons')
        route = Client.routes().route_for(rel)
        url   = route.url_for()

        request = Client.get(url)

        return request

    @staticmethod
    def retrieve(_id, params=None):
        """
        Retrieve the instance of an Account Addon

        :param _id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}

        rel   = Client.rel_for('rels/account-addon')
        route = Client.routes().route_for(rel)
        url   = route.url_for(args={**params, **{'id': _id}})

        request = Client.get(url)

        return request

    @staticmethod
    def update(_id, params=None):
        """
        Update an existing Account Addon

        :param _id: int
        :param params: disc
        :return: Response
        """
        if params is None:
            params = {}

        request_body = {
            "account_addon": params
        }

        headers = {
            'Content-Type': 'application/json'
        }

        rel   = Client.rel_for('rels/account-addon')
        route = Client.routes().route_for(rel)
        url   = route.url_for(args={**params, **{'id': _id}})

        request = Client.put(url, headers=headers, data=json.dumps(request_body))

        return request
