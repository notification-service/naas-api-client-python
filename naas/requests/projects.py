from naas.client import Client


class Projects:

    @staticmethod
    def list(params=None):
        """
        Retrieve the list of projects

        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/projects')
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
        if params is None:
            params = {}
        rel = Client.rel_for('rels/projects')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'id': _id}})
        request = Client.get(url)
        return request

    @staticmethod
    def create(params=None):
        """
        Create a new project

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
        rel = Client.rel_for('rels/projects')
        route = Client.routes().route_for(rel)
        url = route.url_for()
        request = Client.post(url, headers=headers, data=request_body)
        return request

    @staticmethod
    def update(_id, params=None):
        """
        Update an existing project

        :param _id: int
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
        rel = Client.rel_for('rels/project')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={**params, **{'id': _id}})
        request = Client.put(url, headers=headers, data=request_body)
        return request
