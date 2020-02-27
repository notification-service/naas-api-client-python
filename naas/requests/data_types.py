import json
from naas.client import Client
from naas.errors import RecordNotFoundError


class DataTypes:

    @staticmethod
    def list(params=None):
        """
        Retrieve the list of projects

        :param params: dict
        :return: Response
        """
        if not params:
            params = {}

        rel = Client.rel_for('rels/data-types')
        route = Client.routes().route_for(rel)
        url = route.url_for(params)
        request = Client.get(url)
        return request

    @staticmethod
    def retrieve(_id, params=None):
        """
        Retrieve the instance of a project

        :param _id: int
        :param params: dict
        :return: Response
        """
        if not params:
            params = {}

        rel = Client.rel_for('rels/data-type')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'id': _id}})
        request = Client.get(url)
        return request
