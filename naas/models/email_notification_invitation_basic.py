import naas
from naas.configuration import Configuration
from naas.models.email_notification import EmailNotification
import naas.requests.email_notification_invitation_basics as EmailNotificationBasicRequest


class EmailNotificationInvitationBasic(object):
    """

    Email Notification Invitation Basic
    ===============

    This returns an instance of the email notification basic domain model
    """

    @staticmethod
    def create(email_address, project_id, campaign_id, campaign_email_template_id, sender_email_address, from_name, content=None, options=None):
        """
        Helper method to create from the request
        :param email_address: str
        :param project_id: str
        :param campaign_id: str
        :param campaign_email_template_id: str
        :param sender_email_address_id: str
        :param from_name: str
        :param content: dict
        :param options: dict
        :return: EmailNotification
        """
        request = EmailNotificationBasicRequest.EmailNotificationInvitationBasics.create_from_attributes(email_address, project_id, campaign_id, campaign_email_template_id, sender_email_address, from_name, content, options)

        if request:
            return EmailNotification(request.json().get('data'))

        Configuration(
            {
                "logger": (f"Failure retrieving the email notification {request.status_code}")
            }
        )
