from naas.client import Client


class CampaignEmailTemplates:

    @staticmethod
    def list_by_project_id_and_campaign_id(
            project_id, campaign_id, params=None):
        """
        Retrieve the list of a campaign email template by campaign

        :param project_id: str
        :param campaign_id: str
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/project-campaign-campaign-email-templates')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={
            **params, **{'project_id': project_id, 'campaign_id': campaign_id}
        })
        request = Client.get(url)
        return request

    @staticmethod
    def retrieve_by_project_id_and_campaign_id(
            project_id, campaign_id, _id, params=None):
        """
        Retrieve the instance of a campaign email template by campaign

        :param project_id: str
        :param campaign_id: str
        :param id: int
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        rel = Client.rel_for('rels/project-campaign-campaign-email-template')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={
            **params,
            **{
                'project_id': project_id,
                'campaign_id': campaign_id,
                'id': _id
            }
        })
        request = Client.get(url)
        return request

    @staticmethod
    def create_by_project_id_and_campaign_id(
            project_id, campaign_id, params=None):
        """
        Create a new record

        :param project_id: str
        :param campaign_id: str
        :param params: dict
        :return: Response
        """
        if params is None:
            params = {}
        request_body = {
            "campaign_email_template": params
        }
        rel = Client.rel_for('rels/projects')
        route = Client.routes().route_for(rel)
        url = route.url_for(args={
            **params, **{'project_id': project_id, 'campaign_id': campaign_id}
        })

        request = Client.post(url, data=request_body)
        return request
