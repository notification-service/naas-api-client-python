from naas.configurations.default import DefaultConfiguration


class Configuration:

    def __init__(self, attributes=None):
        """
        Create a new instance of the Configuration object.
        This will be initialized with user-supplied values
        or fall back to the Default configuration object

        Example
        >>> configuration = Configuration({'access_token': 'abcd'})
        >>> configuration.access_token
        "abcd"

        :param attributes: dict of configuration keys and values
        """
        if attributes is None:
            attributes = {}
        for key in self.keys():
            setattr(
                self,
                key,
                attributes.get(
                    key,
                    self.options()[key]
                )
            )

    @staticmethod
    def keys():
        """
        Returns the set of allows configuration options

        :return: list Configuration keys
        """
        return [
            'api_host',
            'access_token',
            'connection_options',
            'user_agent',
            'media_type',
            'content_type',
            'request_logger',
            'cache_logger',
            'logger'
        ]

    def connection_options(self):
        """
        The final set of connection options..

        :return: dict Connection options
        """
        return {
            'headers': {
                'accept': self.media_type,
                'user_agent': self.user_agent,
                'content_type': self.content_type
            }
        }

    def configure(self):
        """
        Allows you to configure the object after it's been initialized.

        :return: Configuration The configuration instance
        """
        return self

    def reset(self):
        """
        This allows you to reset your configuration back to the default state
        :return: Configuration The configuration with Defaults applied
        """
        for key in self.keys():
            setattr(self, key, self.options()[key])

    def options(self):
        """
        Return the collection of default options and values
        :return: dict Keys and Values of default configuration
        """
        config = {}
        for key in self.keys():
            config[key] = eval('DefaultConfiguration.' + key + '()')
        return config
