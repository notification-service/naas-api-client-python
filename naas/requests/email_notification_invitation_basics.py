import json
from naas.client import Client


class EmailNotificationInvitationBasics:

    @classmethod
    def create(cls, params=None):
        """
        Create a new record

        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}

        request_body = {
            "email_notification_invitation_basic": params
        }

        request_headers = {
            "Content-Type": "application/json"
        }

        rel   = Client.rel_for('rels/email-notification-invitation-basic')
        route = Client.routes().route_for(rel)
        url   = route.url_for()

        request = Client.post(url, headers=request_headers, data=json.dumps(request_body))

        return request

    @classmethod
    def create_from_attributes(cls, email_address, project_id, campaign_id, campaign_email_template_id, sender_email_address, from_name=None, content=None, options=None):
        """
        Provides a simpler set of arguments to create
        the basic notification

        :param email_address: str
        :param project_id: str
        :param campaign_id: str
        :param campaign_email_template_id: str
        :param sender_email_address: str
        :param from_name: str
        :param content: dict
        :param options: dict
        :return: Response
        """
        if content is None:
            content = {}

        if options is None:
            options = {}

        record_attributes = {
            "email_address": email_address,
            "project_id": project_id,
            "campaign_id": campaign_id,
            "campaign_email_template_id": campaign_email_template_id,
            "content": content,
            "sender_email_address": sender_email_address,
            "from_name": from_name
        }
        record_attributes.update({"tags": options.get("tags", {})})

        if 'account_smtp_setting_id' in options:
            record_attributes.update(
                {"account_smtp_setting_id": options["account_smtp_setting_id"]}
            )

        if 'from_name' in options:
            record_attributes.update({ "from_name": options["from_name"] })

        return cls.create(record_attributes)
