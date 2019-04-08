from naas.client import Client


class Accounts:

    @staticmethod
    def retrieve(params=None):
        """
        Retrieve the current account

        :param params: dict
        :return: Response
        """
        rel = Client.rel_for('rels/account')
        route = Client.routes().route_for(rel)
        url = route.url_for()
        request = Client.get(url)
        return request

    @staticmethod
    def update(params=None):
        """
        Update the current account

        :param params: dict Attributes for the domain model
        :return: Response
        """
        if params is None:
            params = {}
        request_body = {
            "account": params
        }
        headers = {
            'Content-Type': 'application/json'
        }
        rel = Client.rel_for('rels/project')
        route = Client.routes().route_for(rel)
        url = route.url_for()
        request = Client.put(url, headers=headers, data=request_body)
        return request
