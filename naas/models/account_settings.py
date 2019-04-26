import naas
from naas.configuration import Configuration
from naas.models.account_setting import AccountSetting


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
        request = naas.requests.AccountSettings.retrieve()
        if request:
            response_data = request.json().get('data')
            return AccountSetting(response_data)

        Configuration.logger.error(
            f"Failure retrieving the account settings {request.status_code}"
        )
