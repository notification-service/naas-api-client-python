import json
from naas.client import Client


class ProjectSubscriberProperties:

    @staticmethod
    def list_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, params=None):
        """
        Retrieve the list of properties by project

        :param project_id: int
        :param project_subscriber_id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}

        rel = Client.rel_for('rels/project-subscriber-properties')
        route = Client.routes().route_for(rel)
        url = route.url_for(
            args={
                **params,
                **{
                    'project_id': project_id,
                    'project_subscriber_id': project_subscriber_id
                }
            }
        )
        request = Client.get(url)
        return request

    @staticmethod
    def retrieve_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, _id, params=None):
        """
        Retrieve the instance of a project property by project

        :param _id: int
        :param project_id: int
        :param project_subscriber_id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}

        rel = Client.rel_for('rels/project-subscriber-property')
        route = Client.routes().route_for(rel)
        url = route.url_for(
            args={
                **params,
                **{
                    'id': _id,
                    'project_id': project_id,
                    'project_subscriber_id': project_subscriber_id
                }
            }
        )
        request = Client.get(url)
        return request

    @staticmethod
    def create_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, params=None):
        """
        Create a new record

        :param project_id: int
        :param project_subscriber_id: int
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
        rel = Client.rel_for('rels/project-subscriber-properties')
        route = Client.routes().route_for(rel)
        url = route.url_for(
            args={
                **params,
                **{
                    'project_id': project_id,
                    'project_subscriber_id': project_subscriber_id
                }
            }
        )
        request = Client.post(
            url, headers=headers, data=json.dumps(request_body))
        return request

    @staticmethod
    def update_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, _id, params=None):
        """
        Update an existing record

        :param _id: int
        :param project_id: int
        :param project_subscriber_id: int
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
        rel = Client.rel_for('rels/project-subscriber-property')
        route = Client.routes().route_for(rel)
        url = route.url_for(
            args={
                **params,
                **{
                    'id': _id,
                    'project_id': project_id,
                    'project_subscriber_id': project_subscriber_id
                }
            }
        )
        request = Client.put(
            url, headers=headers, data=json.dumps(request_body))
        return request
