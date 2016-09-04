from django.db import models
from django.utils.six import python_2_unicode_compatible
from django.utils.translation import ugettext_lazy as _
from grimoire.django.tracked.models import TrackedLive, TrackedLiveQuerySet


class CatalogQuerySet(TrackedLiveQuerySet):
    """
    Los elementos de catalogo a priori se filtran para excuir aquellos que no estan habilitados
      (ejemplo: una provincia, ciudad, o codigo de SRI que deje de utilizarse). En el administrador,
      sin embargo, usaremos el queryset <Modelo>.objects.with_disabled().
    """

    def with_disabled(self):
        return super(CatalogQuerySet, self).all()

    def all(self):
        return super(CatalogQuerySet, self).filter(enabled=True)


class CatalogManager(models.Manager):
    """
    Manager con unas pocas definiciones de helper.
    """

    def get_by_natural_key(self, code):
        return self.get(code=code)


@python_2_unicode_compatible
class CatalogModel(TrackedLive):
    """
    Elementos de catalogo. Se caracterizan por ser habilitables/deshabilitables, tener un codigo, y algunas notas
      descriptivas. De forma predetermianda se representan por su descripcion.
    """

    name = models.CharField(max_length=100, blank=False, verbose_name=_("Name"),
                            help_text=_("A descriptive text for the element (100 characters)"))
    code = models.SlugField(max_length=30, blank=False, unique=True, verbose_name=_("Code"),
                            help_text=_("An internal code for the element (10 alphanumeric characters or "
                                        "hyphens/underscores). The code must not repeat on different records"))
    enabled = models.BooleanField(default=True, verbose_name=_("Enabled"),
                                  help_text=_("When set to False, this element cannot be used anymore when picking "
                                              "these elements as related values in the corresponding fields"))
    notes = models.TextField(default='', blank=True, verbose_name=_('Additional Notes'),
                             help_text=_('Optional internal notes to add to the element. Usually they '
                                         'determine the meaning of the element.'))
    objects = CatalogManager.from_queryset(CatalogQuerySet)()

    def natural_key(self):
        return self.code,

    def to_string(self):
        return self.name

    def __str__(self):
        return self.to_string()

    class Meta:
        abstract = True
        ordering = ('name',)
