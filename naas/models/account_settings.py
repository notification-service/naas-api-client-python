import logging

from requests import AccountSettings


class AccountSettings(object):
    """

    Account Settings
    ===============

    This returns an instance of the account settings domain model
    """

    @staticmethod
    def retrieve():
        request = AccountSettings.retrieve()
        if request:
            response_data = request.json().get('data')
            return AccountSetting(response_data)

        logging.error(
            f"Failure retrieving the account settings  {request.status_code}"
        )
        return None
