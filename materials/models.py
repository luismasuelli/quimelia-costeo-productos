from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator
from django.db import models
from django.utils.translation import ugettext as _
from catalog.models import CatalogModel



class WorkForce(CatalogModel):

    hourly_price = models.DecimalField(max_digits=7, decimal_places=3, validators=[MinValueValidator(0.001)],
                                       verbose_name=_('Hourly Price'))

    class Meta:
        verbose_name = _('Work Force')
        verbose_name_plural = _('Work Forces')
        permissions = (
            ('list_workforce', 'Can list Work Force'),
            ('view_workforce', 'Can view Work Force'),
        )


class Packaging(CatalogModel):

    price = models.DecimalField(max_digits=7, decimal_places=3, validators=[MinValueValidator(0.001)],
                                verbose_name=_('Price'))

    class Meta:
        verbose_name = _('Packaging')
        verbose_name_plural = _('Packagings')
        permissions = (
            ('list_packaging', 'Can list Packaging'),
            ('view_packaging', 'Can view Packaging'),
        )


class Label(CatalogModel):
    """
    Products may have a label. It is not mandatory since industrial products will not have.
      However, each label will have its price.
    """

    price = models.DecimalField(max_digits=7, decimal_places=3, validators=[MinValueValidator(0.001)],
                                verbose_name=_('Price'))

    class Meta:
        verbose_name = _('Label')
        verbose_name_plural = _('Labels')
        permissions = (
            ('list_label', 'Can list Label'),
            ('view_label', 'Can view Label'),
        )


class RawMaterial(CatalogModel):

    SPECIAL_TYPE_WATER = 'water'
    SPECIAL_TYPES = (
        (SPECIAL_TYPE_WATER, _(u'Water')),
    )

    special = models.CharField(max_length=10, choices=SPECIAL_TYPES, null=True, blank=True)
    kg_price = models.DecimalField(max_digits=7, decimal_places=3, validators=[MinValueValidator(0.001)],
                                   verbose_name=_('Price per Kg'))

    class Meta:
        verbose_name = _('Raw Material')
        verbose_name_plural = _('Raw Materials')
        permissions = (
            ('list_rawmaterial', 'Can list Raw Material'),
            ('view_rawmaterial', 'Can view Raw Material'),
        )

    def clean(self):
        if self.special:
            if type(self).objects.exclude(pk=self.pk).filter(special=self.special).exists():
                raise ValidationError(_(u'Only one raw material can be selected as %s') % self.get_special_display())
            if not self.enabled:
                raise ValidationError(_(u'%s raw material cannot be disabled') % self.get_special_display())
