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
        rel = Client.rel_for('rels/project-campaigns')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'project_id': project_id}})
        request = Client.get(url)
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

        rel = Client.rel_for('rels/project-campaign')
        route = Client.routes().route_for(rel)
        url = route.url_for(
            args={**params, **{'project_id': project_id, 'id': _id}})
        request = Client.get(url)
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

        rel = Client.rel_for('rels/project-campaigns')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'project_id': project_id}})
        request_body = {
            "campaign": params
        }
        request = Client.post(url, data=request_body)
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

        request_body = {
            "campaign": params
        }

        rel = Client.rel_for('rels/project-campaign')
        route = Client.routes().route_for(rel)
        url = route.url_for(
            args={**params, **{'project_id': project_id, 'id': _id}})

        request = Client.put(url, data=request_body)
        return request
