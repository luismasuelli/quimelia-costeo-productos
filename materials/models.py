from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext as _
from grimoire.django.tracked.models import TrackedLive
import re
from support.validators.regex import NameRegexValidator
from django.core.validators import RegexValidator
from catalog.models import CatalogModel
from catalog.fields import CatalogFK


class WorkForce(CatalogModel):

    hourly_price = models.DecimalField(max_digits=7, decimal_places=3, verbose_name=_('Hourly Price'))


class Packaging(CatalogModel):

    price = models.DecimalField(max_digits=7, decimal_places=3, verbose_name=_('Price'))


class RawMaterial(CatalogModel):

    SPECIAL_TYPE_WATER = 'water'
    SPECIAL_TYPES = (
        (SPECIAL_TYPE_WATER, _(u'Water')),
    )

    special = models.CharField(max_length=10, choices=SPECIAL_TYPES, null=True, blank=True)
    kg_price = models.DecimalField(max_digits=7, decimal_places=3, verbose_name=_('Price per Kg'))

    def clean(self):
        if self.special:
            if type(self).objects.exclude(pk=self.pk).filter(special=self.special).exists():
                raise ValidationError(_(u'Only one raw material can be selected as %s') % self.get_special_display())
            if not self.enabled:
                raise ValidationError(_(u'%s raw material cannot be disabled') % self.get_special_display())
