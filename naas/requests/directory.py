from naas.client import Client

class Directory(object):
    @classmethod
    def retrieve(cls):
        """Retrieve the directory request"""
        request = Client.get(Client.api_host())
        return request
