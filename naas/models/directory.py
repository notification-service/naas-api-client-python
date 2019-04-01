import naas
import requests

from naas.models import Links


class Directory(object):
    def __init__(self, attributes={}):
        self.attributes = attributes

    @classmethod
    def retrieve(cls):
        """Retrieve the directory listing"""
        request = naas.requests.Directory.retrieve()

        if request.status_code == requests.codes.ok:
            response_data = request.json()['data']
            return cls(response_data)
        else:
            return None

    def title(self):
        """Returns the title"""
        return self.attributes.get('title', None)

    def description(self):
        """Returns the description"""
        return self.attributes.get('description', None)

    def version(self):
        """Returns the version"""
        return self.attributes.get('version', None)

    def links_attributes(self):
        """Returns the links collection attributes"""
        return self.attributes.get('links', [])

    def links(self):
        """Returns the Links model"""
        return Links(self.links_attributes())
