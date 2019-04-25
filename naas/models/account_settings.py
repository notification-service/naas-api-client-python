from naas.configuration import Configuration
from naas.models import AccountSetting
from naas.requests import AccountSettings


class AccountSettings(object):
    """

    Account Settings
    ===============

    This returns an instance of the account settings domain model
    """

    @staticmethod
    def retrieve():
        """
        Helper method to retrieve from the request

        :return: AccountSetting
        """
        request = AccountSettings.retrieve()
        if request:
            response_data = request.json().get('data')
            return AccountSetting(response_data)

        Configuration.logging.error(
            f"Failure retrieving the account settings {request.status_code}"
        )
