from catalog.admin import CatalogAdmin
from .models import RawMaterial, WorkForce, Packaging


class WorkForceAdmin(CatalogAdmin):
    list_display = ('id', 'code', 'created_on', 'updated_on', 'name', 'hourly_price', 'enabled', 'notes')


class PackagingAdmin(CatalogAdmin):
    list_display = ('id', 'code', 'created_on', 'updated_on', 'name', 'price', 'enabled', 'notes')


class RawMaterialAdmin(CatalogAdmin):
    list_display = ('id', 'code', 'created_on', 'updated_on', 'name', 'kg_price', 'get_special_display',
                    'enabled', 'notes')


def register(site):
    site.register(WorkForce, WorkForceAdmin)
    site.register(Packaging, PackagingAdmin)
    site.register(RawMaterial, RawMaterialAdmin)

