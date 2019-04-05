from naas.client import Client


class EmailNotificationStatuses:

    @staticmethod
    def retrieve_by_email_notification_id(email_notification_id, params=None):
        """
        Retrieve the instance of an email notification status by
        email notification

        :param email_notification_id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for(
            'rels/email-notification-email-notification-delivery-status'
        )
        route = Client.routes().route_for(rel)
        url = route.url_for(
            args=params.update(
                {
                    'email_notification_id': email_notification_id
                }
            )
        )
        request = Client.get(url)
        return request
