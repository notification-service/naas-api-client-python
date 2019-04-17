from nass.configuration import Configuration
from naas.errors import InvalidRequestError, RecordNotFoundError
from nass.models import CampaignEmailTemplate, Error
from naas.requests import CampaignEmailTemplates


class CampaignEmailTemplates(object):
    """

    Campaign Email Templates
    ===============

    This returns an instance of the campaign email temaplates model
    """

    def __init__(self, collection):
        self.collection = list(collection)
        self.index = len(self.collection)

    def __iter__(self):
        """ Implement iterator """
        return map(lambda r: CampaignEmailTemplate(r), self.collection)

    def next(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.collection[self.index]

    @classmethod
    def list_by_project_id_and_campaign_id(project_id, campaign_id, params=None):
        if params is None:
            params = {}

        request = CampaignEmailTemplates.list_by_project_id_and_campaign_id(
            project_id, campaign_id, params)

        klass_attributes = []

        if request:
            klass_attributes = request.json().get('data')
        else:
            Configuration.logger.error(
                "Failure retrieving the email templates {request.status_code}")
        return cls(klass_attributes)

    @staticmethod
    def retrieve_by_project_id_and_campaign_id(project_id, campaign_id, id, params=None):
        if params is None:
            params = {}

        request = CampaignEmailTemplates.retrieve_by_project_id_and_campaign_id(
            project_id, campaign_id, id, params)

        if request:
            return CampaignEmailTemplate(request.json().get('data'))
        elif request.status_code == 404:
            raise RecordNotFoundError(f"Could not find record with id {id}")
            return

        Configuration.logger.error(
            f"Failure retrieving the email template {request.status_code}")

    @staticmethod
    def create_by_project_id_and_campaign_id(project_id, campaign_id, params=None):
        request = CampaignEmailTemplates.create_by_project_id_and_campaign_id(
            project_id, campaign_id, params)

        if request:
            return CampaignEmailTemplate(request.json().get('data'))

        error = Error(request.json().get('data'))
        failure_message = (
            f"Failure creating the record {error.full_messages}")

        Configuration.logger.error(failure_message)
        raise InvalidRequestError(failure_message)
