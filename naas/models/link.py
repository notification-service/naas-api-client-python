from uritemplate import URITemplate, expand


class Link(object):
	"""

	Link
	===============

	This returns an instance of the Link domain model
	"""
	def __init__(self, attributes={}):
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

	def url_for(self, args={}):
		"""Returns the URL for this link"""
		if self.templated() == True:
			url = URITemplate(self.href())
			return url.expand(args)
		else:
			return self.href()
