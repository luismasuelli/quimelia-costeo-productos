from catalog.models import CatalogModel
from catalog.fields import CatalogFK
from django.utils.translation import ugettext_lazy as _
from django.utils.six import text_type


class Province(CatalogModel):
    """
    Provincia.
    """

    def to_string(self):
        return text_type("%s") % (super(Province, self).to_string())

    class Meta(CatalogModel.Meta):
        abstract = False
        verbose_name = _("Province")
        verbose_name_plural = _("Provinces")


class City(CatalogModel):
    """
    Ciudad.
    """

    province = CatalogFK(Province, verbose_name=_('Province'))

    def to_string(self):
        return text_type("%s, %s") % (super(City, self).to_string(), self.province)

    class Meta(CatalogModel.Meta):
        abstract = False
        verbose_name = _("City")
        verbose_name_plural = _("Cities")
