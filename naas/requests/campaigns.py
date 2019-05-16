import json
from naas.client import Client
from naas.errors import InvalidRequestError


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
        request_headers = {
            "Content-Type": "application/json"
        }
        request = Client.post(url, headers=request_headers,
                              data=json.dumps(request_body))
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
            "campaign": {**params, **{'project_id': project_id}}
        }
        request_headers = {
            "Content-Type": "application/json"
        }

        rel = Client.rel_for('rels/project-campaign')
        route = Client.routes().route_for(rel)
        url = route.url_for(
            args={**params, **{'project_id': project_id, 'id': _id}})

        request = Client.put(url, headers=request_headers,
                             data=json.dumps(request_body))
        return request

    @staticmethod
    def update_by_project_id_with_attachments(project_id, _id, files):
        """
        Update an existing record with attachments
        :param project_id: string
        :param _id: string
        :param files: dict/list Files to be uploaded with all the details
        :return: Response
        """
        rel = Client.rel_for('rels/project-campaign')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={'project_id': project_id, 'id': _id})

        if files:
            request = Client.put(url, files=files)
            return request
        raise InvalidRequestError("No files provided")
