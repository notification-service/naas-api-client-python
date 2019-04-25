from naas.client import Client


class EmailNotificationDeliveries:

    @staticmethod
    def list_by_email_notification_id(email_notification_id, params=None):
        """
        Retrieve the list of deliveries by the email notification

        :param email_notification_id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for(
            'rels/email-notification-email-notification-deliveries'
        )
        route = Client.routes().route_for(rel)
        url = route.url_for(args={
            **params, **{'email_notification_id': email_notification_id}})
        request = Client.get(url)
        return request

    @staticmethod
    def retrieve_by_email_notification_id(
            email_notification_id, _id, params=None):
        """
        Retrieve the instance of an email notification delivery by
        email notification

        :param email_notification_id: int
        :param _id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for(
            'rels/email-notification-email-notification-delivery'
        )
        route = Client.routes().route_for(rel)
        url = route.url_for(args={
            **params,
            **{'email_notification_id': email_notification_id, 'id': _id}
        })
        request = Client.get(url)
        return request
