from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import ugettext as _
from grimoire.django.tracked.models import TrackedLive
import re
from .validators.regex import NameRegexValidator
from django.core.validators import RegexValidator
from catalog.models import CatalogModel
from catalog.fields import CatalogFK
from geo.models import City


class EntityCountry(CatalogModel):
    """
    Entity Country (to match a passport against)
    """

    SPECIAL_TYPE_HOMELAND = 'homeland'
    SPECIAL_TYPES = (
        (SPECIAL_TYPE_HOMELAND, _(u'Homeland')),
    )

    special = models.CharField(max_length=10, choices=SPECIAL_TYPES, null=True, blank=True)

    def is_homeland(self):
        return self.special == self.SPECIAL_TYPE_HOMELAND

    def clean(self):
        if self.is_homeland():
            if type(self).objects.exclude(pk=self.pk).filter(special=self.SPECIAL_TYPE_HOMELAND).exists():
                raise ValidationError(_(u'Only one country can be selected as homeland'))
            if not self.enabled:
                raise ValidationError(_(u'Homeland country cannot be disabled'))


def default_country():
    return EntityCountry.objects.get(special=EntityCountry.SPECIAL_TYPE_HOMELAND).code


class Entity(TrackedLive):
    """
    Entity (With a ruc, ID, or passport).
    """

    ID_TYPE_NATIONAL = 1
    ID_TYPE_FOREIGN = 2
    ID_TYPES = (
        (ID_TYPE_NATIONAL, _('Citizen ID')),
        (ID_TYPE_FOREIGN, _('Passport'))
    )
    identification = models.CharField(max_length=13, verbose_name=_('Identification'),
                                      validators=[RegexValidator(r'^\d*$')])
    identification_type = models.PositiveSmallIntegerField(null=False, choices=ID_TYPES)
    identification_country = CatalogFK(EntityCountry, null=False, default=default_country)
    name = models.CharField(max_length=70, validators=[NameRegexValidator(
        mode=NameRegexValidator.MODE_ALPHANUMERIC_EXTENDED
    )], verbose_name=_('Name'))
    address = models.CharField(max_length=128, verbose_name=_('Address'))
    city = CatalogFK(City, verbose_name=_('City'))

    def in_homeland(self):
        return self.identification_country.is_homeland()

    def clean(self):
        try:
            in_homeland = self.in_homeland()
        except EntityCountry.DoesNotExist:
            return

        if self.identification_type == self.ID_TYPE_NATIONAL:
            if not in_homeland:
                raise ValidationError(_(u'A foreign country must not be chosen for a local identification'))

            if not re.match('^\d{10}(\d{3})?$', self.identification):
                raise ValidationError(_(u'Ecuadorean identifier ID must be 10 or 13 digits long'))

            coeficientes = [2, 1, 2, 1, 2, 1, 2, 1, 2]
            digits = [int(v) for v in self.identification[:9]]
            reduce9 = lambda x: x - 9 if x > 9 else x
            reduced = [reduce9(a * b) for (a, b) in zip(coeficientes, digits)]
            weighted = sum(reduced)
            modulo = weighted % 10
            modulo = (10 - modulo) if modulo != 0 else 0
            province = int(self.identification[:2])
            verifier = int(self.identification[9])
            person_type = int(self.identification[2])

            if province not in xrange(1, 25):
                raise ValidationError(_(u'Invalid ecuadorean identifier'), 'invalid-content')

            if person_type not in xrange(0, 6):
                raise ValidationError(_(u'Invalid ecuadorean identifier'), 'invalid-content')

            if verifier != modulo:
                raise ValidationError(_(u'Invalid ecuadorean identifier'), 'invalid-content')
        elif self.identification_type == self.ID_TYPE_FOREIGN:
            if not in_homeland:
                raise ValidationError(_(u'A foreign country must be chosen for a passport identification'))
            if not re.match(r'^[a-zA-Z0-9]{8,}$', self.identification):
                raise ValidationError(_(u'Invalid passport'), 'invalid-content')

    class Meta:
        unique_together = (('identification_country', 'identification'),)
        verbose_name = _('Entity')
        verbose_name_plural = _('Entities')
        permissions = (
            ('list_entity', 'List Entity'),
            ('view_entity', 'View Entity'),
        )


class ServiceArea(CatalogModel):
    """
    Service Area.
    """

    class Meta:
        verbose_name = _('Service Area')
        verbose_name_plural = _('Service Areas')


class ClientAccount(TrackedLive):
    """
    A client account involves an entity (which may be a natural person or not).
    """

    service_area = CatalogFK(ServiceArea, on_delete=models.PROTECT, verbose_name=_('Service Area'))
    entity = models.ForeignKey(Entity, on_delete=models.CASCADE, verbose_name=_('Entity'))

    class Meta:
        unique_together = (('service_area', 'entity'),)
        verbose_name = _('Client Account')
        verbose_name_plural = _('Client Accounts')
        permissions = (
            ('list_clientaccount', 'List Client Account'),
            ('view_clientaccount', 'View Client Account'),
        )
