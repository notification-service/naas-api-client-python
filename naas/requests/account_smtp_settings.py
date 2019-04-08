from naas.client import Client
from naas.errors import RecordNotFoundError


class AccountSmtpSettings:

    @staticmethod
    def list(params=None):
        """
        Retrieve the list of SMTP settings

        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/smtp-settings')
        route = Client.routes().route_for(rel)
        url = route.url_for(params)
        request = Client.get(url)
        return request

    @staticmethod
    def retrieve(_id, params=None):
        """
        Retrieve the instance of an SMTP setting

        :param _id: int
        :param params: dict
        :raises RecordNotFoundError
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/smtp-setting')
        route = Client.routes().route_for(rel)
        url = route.url_for(args=params.update({'id': _id}))

        try:
            request = Client.get(url)
            request.raise_for_status()
        except Exception:
            raise RecordNotFoundError(request.json())
        return request

    @staticmethod
    def create(params=None):
        """
        Created a new record

        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        request_body = {
            "smtp_settings": params
        }
        rel = Client.rel_for('rels/smtp-settings')
        route = Client.routes().route_for(rel)
        url = route.url_for()
        request = Client.post(url, data=request_body)
        return request
