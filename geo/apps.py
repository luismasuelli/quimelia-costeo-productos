from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class GeoAppConfig(AppConfig):

    verbose_name = _('Geographic Data')
    name = 'geo'
    label = 'geo'
