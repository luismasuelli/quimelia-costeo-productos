from catalog.admin import CatalogAdmin
from .models import Province, City


class ProvinceAdmin(CatalogAdmin):
    list_display = ('id', 'code', 'created_on', 'updated_on', 'name', 'enabled', 'notes')


class CityAdmin(CatalogAdmin):
    list_display = ('id', 'code', 'created_on', 'updated_on', 'name', 'enabled', 'notes', 'province')


def register(site):
    site.register(Province, ProvinceAdmin)
    site.register(City, CityAdmin)
