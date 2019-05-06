import naas
from naas.configuration import Configuration
from naas.models.email_notification import EmailNotification


class EmailNotificationBasic(object):
    """

    Email Notification Basic
    ===============

    This returns an instance of the email notification basic domain model
    """

    @staticmethod
    def create(
            email_address, project_id, campaign_id,
            campaign_email_template_id, content=None, options=None
    ):
        """
        Helper method to create from the request
        :param email_address: str
        :param project_id
        :param campaign_id str
        :param campaign_email_template_id
        :param content: dict
        :param options: dict
        :return: EmailNotification
        """
        request = naas.requests.EmailNotificationBasics.create_from_attributes(
            email_address, project_id, campaign_id,
            campaign_email_template_id, content, options
        )

        if request:
            return EmailNotification(request.json().get('data'))

        Configuration(
            {
                "logger": ("Failure retrieving the email "
                           f"notification {request.status_code}")
            }
        )
