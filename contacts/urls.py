from django.conf.urls import url, include
from . import views


app_name = 'contacts'
urlpatterns = [
    url(r'^entities$', views.EntitiesList.as_view(template_name='contacts/entities_list.html', paginate_by=10,
                                                  search_form_label='Buscar'), name='entities-list'),
    url(r'^entities/create$', views.EntityCreate.as_view(template_name='contacts/entities_create.html'),
        name='entities-create'),
    url(r'^entities/(?P<pk>\d+)$', views.EntityDetail.as_view(template_name='contacts/entities_view.html'),
        name='entities-detail'),
    url(r'^entities/(?P<pk>\d+)/update$', views.EntityUpdate.as_view(template_name='contacts/entities_update.html'),
        name='entities-update'),
    url(r'^entities/(?P<pk>\d+)/delete$', views.EntityDelete.as_view(template_name='contacts/entities_delete.html'),
        name='entities-delete'),
    # TODO poner estas bien!!!
    url(r'^client-accounts$', views.EntitiesList, name='entities-list'),
    url(r'^client-accounts/create$', views.EntityCreate, name='entities-create'),
    url(r'^client-accounts/(?P<pk>\d+)$', views.EntityDetail, name='entities-detail'),
    url(r'^client-accounts/(?P<pk>\d+)/update$', views.EntityUpdate, name='entities-update'),
    url(r'^client-accounts/(?P<pk>\d+)/delete$', views.EntityDelete, name='entities-delete'),
]
