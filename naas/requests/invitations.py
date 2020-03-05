import json
from naas.client import Client


class Invitations:

    @staticmethod
    def list(params=None):
        """
        Retrieve the list of Invitations

        :param params: dict
        :return: Response
        """
        rel   = Client.rel_for('rels/invitations')
        route = Client.routes().route_for(rel)
        url   = route.url_for()

        request = Client.get(url)

        return request

    @staticmethod
    def retrieve(_id, params=None):
        """
        Retrieve the instance of an Invitation

        :param _id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}

        rel   = Client.rel_for('rels/invitation')
        route = Client.routes().route_for(rel)
        url   = route.url_for(args={**params, **{'id': _id}})

        request = Client.get(url)

        return request

    @staticmethod
    def accept(_id, params=None):
        """
        Accpet an existing Invitation

        :param _id: int
        :param params: disc
        :return: Response
        """
        if params is None:
            params = {}

        rel   = Client.rel_for('rels/invitation-accept')
        route = Client.routes().route_for(rel)
        url   = route.url_for(args={**params, **{'id': _id}})

        request = Client.post(url)

        return request

    @staticmethod
    def decline(_id, params=None):
        """
        Decline an existing Invitation

        :param _id: int
        :param params: disc
        :return: Response
        """
        if params is None:
            params = {}

        rel   = Client.rel_for('rels/invitation-decline')
        route = Client.routes().route_for(rel)
        url   = route.url_for(args={**params, **{'id': _id}})

        request = Client.post(url)

        return request
