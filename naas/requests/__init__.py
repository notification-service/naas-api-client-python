"""

naas.requests
=====

The NAAS API Client Requests

"""

from naas.requests.accounts import Accounts
from naas.requests.account_settings import AccountSettings
from naas.requests.account_smtp_settings import AccountSmtpSettings
from naas.requests.campaign_email_templates import CampaignEmailTemplates
from naas.requests.directory import Directory
from naas.requests.projects import Projects
from naas.requests.subscriber_email_addresses import SubscriberEmailAddresses
from naas.requests.subscribers import Subscriber
from naas.requests.email_notification_basics import EmailNotificationBasics
from naas.requests.email_notification_deliveries import (
    EmailNotificationDeliveries
)
from naas.requests.email_notification_statuses import EmailNotificationStatuses
from naas.requests.email_notifications import EmailNotifications
