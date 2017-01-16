from django.apps import AppConfig
from django.utils.translation import ugettext_lazy as _


class MaterialsAppConfig(AppConfig):

    verbose_name = _('Raw Materials and Other Costs')
    name = 'materials'
    label = 'materials'
