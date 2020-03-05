import iso8601


class SubscriberProjectProperty(object):
    """

    Subscriber Project Property
    ===========================

    This returns an instance of the Subscriber Project Property domain model
    """

    def __init__(self, attributes={}):
        self.attributes = attributes

    def project_property_id(self):
        """Returns the subscriber project property project_property_id"""
        return self.attributes.get('project_property_id')

    def project_subscriber_property_id(self):
        """Returns the subscriberprojectproperty project_subscriber_property_id"""
        return self.attributes.get('project_subscriber_property_id')

    def subscriber_provided_value(self):
        """Returns a boolean after checking the subscriber_provided_value"""
        if self.project_subscriber_property_id():
            return True
        return False

    def name(self):
        """Returns the data type name"""
        return self.attributes.get('name')

    def key_name(self):
        """Returns the key name"""
        return self.attributes.get('key_name')

    def description(self):
        """Returns the subscriber project property description"""
        return self.attributes.get('description')

    def value(self):
        """Returns the subscriber project property value"""
        return self.attributes.get('description')

    def is_subscriber_editable(self):
        """Returns true if is subscriber editable"""
        return self.attributes.get('is_subscriber_editable')

    def is_subscriber_viewable(self):
        """Returns true if is subscriber viewable"""
        return self.attributes.get('is_subscriber_viewable')
