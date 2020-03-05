import json
from naas.client import Client


class Addons:

    @staticmethod
    def list(params=None):
        """
        Retrieve the list of addons

        :param params: dict
        :return: Response
        """
        rel = Client.rel_for('rels/addons')
        route = Client.routes().route_for(rel)
        url = route.url_for()
        request = Client.get(url)
        return request

    @staticmethod
    def retrieve(_id, params=None):
        """
        Retrieve the instance of an Addon

        :param _id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/addon')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'id': _id}})
        request = Client.get(url)
        return request
