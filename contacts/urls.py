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
    url(r'^entities/(?P<pk>\d+)/client-accounts/create$',
        views.ClientAccountCreate.as_view(template_name='contacts/client_accounts_create.html'),
        name='client-accounts-create'),
    url(r'^entities/(?P<pk>\d+)/client-accounts/(?P<ca_pk>\d+)$',
        views.ClientAccountDetail.as_view(template_name='contacts/client_accounts_view.html'),
        name='client-accounts-detail'),
    url(r'^entities/(?P<pk>\d+)/client-accounts/(?P<ca_pk>\d+)/update$',
        views.ClientAccountUpdate.as_view(template_name='contacts/client_accounts_update.html'),
        name='client-accounts-update'),
    url(r'^entities/(?P<pk>\d+)/client-accounts/(?P<ca_pk>\d+)/delete$',
        views.ClientAccountDelete.as_view(template_name='contacts/client_accounts_delete.html'),
        name='client-accounts-delete'),
]
