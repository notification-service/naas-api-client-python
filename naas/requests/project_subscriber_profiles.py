import json
from naas.client import Client


class ProjectSubscriberProfiles:

    @staticmethod
    def retrieve_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, params=None):
        """
        Retrieve the instance of a project subscriber by project

        :param project_id: int
        :param project_subscriber_id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}

        rel = Client.rel_for('rels/project-subscriber-profile')
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
    def update_by_project_id_and_project_subscriber_id(
            project_id, project_subscriber_id, params=None):
        """
        Update an existing record

        :param project_id: int
        :param project_subscriber_id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        request_body = {
            "project_subscriber_profile": params
        }
        headers = {
            'Content-Type': 'application/json'
        }
        rel = Client.rel_for('rels/project-subscriber-profile')
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
        request = Client.put(
            url, headers=headers, data=json.dumps(request_body))
        return request
