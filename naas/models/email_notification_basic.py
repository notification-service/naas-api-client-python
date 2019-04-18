from nass.models import SubscriberEmailAddress, Error
from naas.requests import EmailNotification


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
        request = EmailNotificationBasics.create_from_attributes(
            email_address, project_id, campaign_id,
            campaign_email_template_id, content, options
        )

        if request:
            return EmailNotification(request.json().get('data'))

        Configuration.logger.error(
            "Failure retrieving the email notification {request.status_code}"
        )
