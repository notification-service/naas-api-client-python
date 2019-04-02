from naas.client import Client


class Campaigns:

    @staticmethod
    def list_by_project_id(project_id, params=None):
        """
        Retrieve the list of campaigns by project
        :param project_id: string
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        route = Client.create_route('rels/project-campaigns')
        request = Client.get(
            route,
            params=params.update({'project_id': project_id})
        )
        return request

    @staticmethod
    def retrieve_by_project_id(project_id, _id, params=None):
        """
        Retrieve the instance of a campaign by project
        :param project_id: string
        :param _id: string
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        route = Client.create_route('rels/project-campaigns')
        request = Client.get(
            route,
            params=params.update(
                {
                    'project_id': project_id,
                    'id': _id
                }
            )
        )
        return request

    @staticmethod
    def create_by_project_id(project_id, params=None):
        """
        Create a new record
        :param project_id: string
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        route = Client.create_route(f'rels/project-campaigns/{project_id}')
        request_body = {
            "campaign": params
        }
        request = Client.post(route, json=request_body)
        return request

    @staticmethod
    def update_by_project_id(project_id, _id, params=None):
        """
        Update an existing record
        :param project_id: string
        :param _id: string
        :param params: dict Attributes for the domain model
        :return: Response
        """
        if params is None:
            params = {}
        route = Client.create_route(
            f'rels/project-campaigns/{project_id}/{_id}'
        )
        request_body = {
            "campaign": params
        }
        headers = {
            'Content-Type': 'application/json'
        }
        request = Client.put(route, headers=headers, json=request_body)
        return request
