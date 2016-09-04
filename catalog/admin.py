from grimoire.django.tracked.admin import TrackedLiveAdmin


###################################################
#
#
#    Se pueden usar los filtros de arriba de la siguiente manera
#
#    class YourAdmin(ModelAdmin):
#       # ...
#       list_filter = (CreatePeriodAgoAndCurrentFilter, UpdatePeriodAgoAndCurrentFilter)
#
#    Considerando que solo tomas UN filtro `Create*` y/o solo UN filtro `Update*`
#    Y por ModelAdmin, vale tambien CatalogAdmin
#
#
###################################################


class CatalogAdmin(TrackedLiveAdmin):
    """
    Todos los modelos van a tener los mismos campos, por lo que tendran un administrador realmente parecido.
    """

    list_display = ('id', 'code', 'created_on', 'updated_on', 'name', 'enabled', 'notes')
    list_display_links = ('id', 'code')

    def get_queryset(self, request):
        return self.model.objects.with_disabled()
