from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class ContactsAppConfig(AppConfig):

    verbose_name = _('Contacts Management')
    name = 'contacts'
    label = 'contacts'
