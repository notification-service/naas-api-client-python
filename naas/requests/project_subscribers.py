import json
from naas.client import Client
from naas.errors import RecordNotFoundError


class ProjectSubscribers:

    @staticmethod
    def list_by_project_id(project_id, params=None):
        """
        Retrieve the list of subscribers by project

        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}

        rel = Client.rel_for('rels/project-subscribers')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'project_id': project_id}})
        request = Client.get(url)
        return request

    @staticmethod
    def retrieve_by_project_id(project_id, params=None):
        """
        Retrieve the instance of a project subscriber by project

        :param _id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}

        rel = Client.rel_for('rels/project-subscriber')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'project_id': project_id}})
        request = Client.get(url)
        return request

    @staticmethod
    def create_by_project_id(project_id, params=None):
        """
        Create a new record

        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        request_body = {
            "project": params
        }
        headers = {
            'Content-Type': 'application/json'
        }
        rel = Client.rel_for('rels/project-subscribers')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'project_id': project_id}})
        request = Client.post(
            url, headers=headers, data=json.dumps(request_body))
        return request
