from uritemplate import URITemplate, expand


class Link(object):
    """

    Link
    ===============

    This returns an instance of the Link domain model
    """
    def __init__(self, attributes=None):
        if attributes is None:
            attributes = {}
        self.attributes = attributes

    def title(self):
        """Returns the title"""
        return self.attributes.get('title', None)

    def href(self):
        """Returns the href"""
        return self.attributes.get('href', None)

    def rel(self):
        """Returns the rel"""
        return self.attributes.get('rel', None)

    def templated(self):
        """Returns the templated"""
        return self.attributes.get('templated', False)

    def url_for(self, args=None):
        """Returns the URL for this link"""
        if args is None:
            args = {}
        if self.templated():
            url = URITemplate(self.href())
            return url.expand(args)
        else:
            return self.href()

    def to_csv(self):
        """Returns the record as CSV"""
        return [self.title(), self.href()]

