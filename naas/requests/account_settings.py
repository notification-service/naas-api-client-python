from naas.client import Client


class AccountSettings:

    @staticmethod
    def retrieve(params=None):
        """
        Retrieve the current account settings

        :param params: dict
        :return: Response
        """
        rel = Client.rel_for('rels/account-settings')
        route = Client.routes().route_for(rel)
        url = route.url_for()
        request = Client.get(url)
        return request

    @staticmethod
    def update(params=None):
        """
        Update the current account settings

        :param params: dict Attributes for the domain model
        :return: Response
        """
        if params is None:
            params = {}
        request_body = {
            "account_settings": params
        }
        headers = {
            'Content-Type': 'application/json'
        }
        rel = Client.rel_for('rels/project')
        route = Client.routes().route_for(rel)
        url = route.url_for()
        request = Client.put(url, headers=headers, data=request_body)
        return request

    @staticmethod
    def enable_send_grid():
        """
        Enable the send grid setting

        :return: Response
        """
        rel = Client.rel_for('rels/account-settings-enable-send-grid')
        route = Client.routes().route_for(rel)
        url = route.url_for()
        request = Client.post(url)
        return request

    @staticmethod
    def disable_send_grid():
        """
        Disable the send grid setting

        :return: Response
        """
        rel = Client.rel_for('rels/account-settings-disable-send-grid')
        route = Client.routes().route_for(rel)
        url = route.url_for()
        request = Client.post(url)
        return request
