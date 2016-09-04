from django.contrib.admin import ModelAdmin
from catalog.admin import CatalogAdmin
from .models import ServiceArea, ClientAccount, Entity


class EntityAdmin(ModelAdmin):
    list_display = ('id', 'identification', 'identification_type', 'name', 'address', 'city')


class ServiceAreaAdmin(CatalogAdmin):
    list_display = ('id', 'code', 'created_on', 'updated_on', 'name', 'enabled', 'notes')


class ClientAccountAdmin(ModelAdmin):
    list_display = ('id', 'service_area', 'entity')


def register(site):
    site.register(Entity, EntityAdmin)
    site.register(ServiceArea, ServiceAreaAdmin)
    site.register(ClientAccount, ClientAccountAdmin)
