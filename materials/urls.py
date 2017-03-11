from django.conf.urls import url, include
from . import views


app_name = 'materials'
urlpatterns = [
    url(r'^workforces$', views.WorkForcesList.as_view(template_name='materials/work_forces_list.html', paginate_by=10,
                                                      search_form_label='Buscar'), name='workforces-list'),
    url(r'^workforces/create$', views.WorkForceCreate.as_view(template_name='materials/work_forces_create.html'),
        name='workforces-create'),
    url(r'^workforces/(?P<pk>\d+)$', views.WorkForceDetail.as_view(template_name='materials/work_forces_view.html'),
        name='workforces-detail'),
    url(r'^workforces/(?P<pk>\d+)/update$', views.WorkForceUpdate.as_view(template_name='materials/work_forces_update.html'),
        name='workforces-update'),
    url(r'^workforces/(?P<pk>\d+)/delete$', views.WorkForceDelete.as_view(template_name='materials/work_forces_delete.html'),
        name='workforces-delete'),

    url(r'^packagings$', views.PackagingsList.as_view(template_name='materials/packagings_list.html', paginate_by=10,
                                                  search_form_label='Buscar'), name='packagings-list'),
    url(r'^packagings/create$', views.PackagingCreate.as_view(template_name='materials/packagings_create.html'),
        name='packagings-create'),
    url(r'^packagings/(?P<pk>\d+)$', views.PackagingDetail.as_view(template_name='materials/packagings_view.html'),
        name='packagings-detail'),
    url(r'^packagings/(?P<pk>\d+)/update$', views.PackagingUpdate.as_view(template_name='materials/packagings_update.html'),
        name='packagings-update'),
    url(r'^packagings/(?P<pk>\d+)/delete$', views.PackagingDelete.as_view(template_name='materials/packagings_delete.html'),
        name='packagings-delete'),

    url(r'^labels$', views.PackagingsList.as_view(template_name='materials/labels_list.html', paginate_by=10,
                                                  search_form_label='Buscar'), name='labels-list'),
    url(r'^labels/create$', views.PackagingCreate.as_view(template_name='materials/labels_create.html'),
        name='labels-create'),
    url(r'^labels/(?P<pk>\d+)$', views.PackagingDetail.as_view(template_name='materials/labels_view.html'),
        name='labels-detail'),
    url(r'^labels/(?P<pk>\d+)/update$', views.PackagingUpdate.as_view(template_name='materials/labels_update.html'),
        name='labels-update'),
    url(r'^labels/(?P<pk>\d+)/delete$', views.PackagingDelete.as_view(template_name='materials/labels_delete.html'),
        name='labels-delete'),

    url(r'^rawmaterials$', views.RawMaterialsList.as_view(template_name='materials/raw_materials_list.html', paginate_by=10,
                                                  search_form_label='Buscar'), name='rawmaterials-list'),
    url(r'^rawmaterials/create$', views.RawMaterialCreate.as_view(template_name='materials/raw_materials_create.html'),
        name='rawmaterials-create'),
    url(r'^rawmaterials/(?P<pk>\d+)$', views.RawMaterialDetail.as_view(template_name='materials/raw_materials_view.html'),
        name='rawmaterials-detail'),
    url(r'^rawmaterials/(?P<pk>\d+)/update$', views.RawMaterialUpdate.as_view(template_name='materials/raw_materials_update.html'),
        name='rawmaterials-update'),
    url(r'^rawmaterials/(?P<pk>\d+)/delete$', views.RawMaterialDelete.as_view(template_name='materials/raw_materials_delete.html'),
        name='rawmaterials-delete'),
]

