from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Count, ProtectedError
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext_lazy as _
from support.search.views import SearchListView
from main.views import BaseContextMixin
from .models import WorkForce, RawMaterial, Packaging
from .forms import WorkForceForm, RawMaterialForm, PackagingForm


class WorkForcesList(BaseContextMixin, PermissionRequiredMixin, SearchListView):
    permission_required = 'materials.list_workforce'
    # queryset = WorkForce.objects.annotate(...)
    search_fields = ('name', 'code', 'notes')
    model = WorkForce


class WorkForceCreate(BaseContextMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'materials.add_workforce'
    form_class = WorkForceForm
    model = WorkForce
    success_url = reverse_lazy('materials:workforces-list')

    def get_success_message(self, cleaned_data):
        return _('Work force "%(name)s" (%(code)s) successfully created') % {
            'name': self.object.name, 'code': self.object.code
        }


class WorkForceUpdate(BaseContextMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'materials.change_workforce'
    form_class = WorkForceForm
    model = WorkForce

    def get_success_message(self, cleaned_data):
        return _('Work force "%(name)s" (%(code)s) successfully updated') % {
            'name': self.object.name, 'code': self.object.code
        }

    def get_success_url(self):
        return reverse('materials:workforces-update', kwargs={'pk': self.object.pk})


class WorkForceDelete(BaseContextMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'materials.delete_workforce'
    model = WorkForce
    success_url = reverse_lazy('materials:workforces-list')

    def post(self, request, *args, **kwargs):
        try:
            result = self.delete(request, *args, **kwargs)
            message = _('Work force "%(name)s" (%(code)s) successfully deleted') % {
                'name': self.object.name, 'code': self.object.code
            }
            messages.success(self.request, message)
            return result
        except ProtectedError:
            message = _('Cannot delete work force "%(name)s" (%(code)s) since it is in use') % {
                'name': self.object.name, 'code': self.object.code
            }
            messages.error(self.request, message)
            return self.get(request, *args, **kwargs)


class WorkForceDetail(BaseContextMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'materials.view_workforce'
    model = WorkForce


class PackagingsList(BaseContextMixin, PermissionRequiredMixin, SearchListView):
    permission_required = 'materials.list_packaging'
    # queryset = Packagings.objects.annotate(...)
    search_fields = ('name', 'code', 'notes')
    model = Packaging


class PackagingCreate(BaseContextMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'materials.add_packaging'
    form_class = PackagingForm
    model = Packaging
    success_url = reverse_lazy('materials:packagings-list')

    def get_success_message(self, cleaned_data):
        return _('Packaging "%(name)s" (%(code)s) successfully created') % {
            'name': self.object.name, 'code': self.object.code
        }


class PackagingUpdate(BaseContextMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'materials.change_packaging'
    form_class = PackagingForm
    model = Packaging

    def get_success_message(self, cleaned_data):
        return _('Packaging "%(name)s" (%(code)s) successfully updated') % {
            'name': self.object.name, 'code': self.object.code
        }

    def get_success_url(self):
        return reverse('materials:packagings-update', kwargs={'pk': self.object.pk})


class PackagingDelete(BaseContextMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'materials.delete_packaging'
    model = Packaging
    success_url = reverse_lazy('materials:packagings-list')

    def post(self, request, *args, **kwargs):
        try:
            result = self.delete(request, *args, **kwargs)
            message = _('Packaging "%(name)s" (%(code)s) successfully deleted') % {
                'name': self.object.name, 'code': self.object.code
            }
            messages.success(self.request, message)
            return result
        except ProtectedError:
            message = _('Cannot delete packaging "%(name)s" (%(code)s) since it is in use') % {
                'name': self.object.name, 'code': self.object.code
            }
            messages.error(self.request, message)
            return self.get(request, *args, **kwargs)


class PackagingDetail(BaseContextMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'materials.view_packaging'
    model = Packaging


class RawMaterialsList(BaseContextMixin, PermissionRequiredMixin, SearchListView):
    permission_required = 'materials.list_rawmaterial'
    # queryset = RawMaterial.objects.annotate(...)
    search_fields = ('name', 'code', 'notes')
    model = RawMaterial


class RawMaterialCreate(BaseContextMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'materials.add_rawmaterial'
    form_class = RawMaterialForm
    model = RawMaterial
    success_url = reverse_lazy('materials:rawmaterials-list')

    def get_success_message(self, cleaned_data):
        return _('Raw material "%(name)s" (%(code)s) successfully created') % {
            'name': self.object.name, 'code': self.object.code
        }


class RawMaterialUpdate(BaseContextMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'materials.change_rawmaterial'
    form_class = RawMaterialForm
    model = RawMaterial

    def get_success_message(self, cleaned_data):
        return _('Raw material "%(name)s" (%(code)s) successfully updated') % {
            'name': self.object.name, 'code': self.object.code
        }

    def get_success_url(self):
        return reverse('materials:rawmaterials-update', kwargs={'pk': self.object.pk})


class RawMaterialDelete(BaseContextMixin, PermissionRequiredMixin, DeleteView):
    permission_required = 'materials.delete_rawmaterial'
    model = RawMaterial
    success_url = reverse_lazy('materials:rawmaterials-list')

    def post(self, request, *args, **kwargs):
        try:
            result = self.delete(request, *args, **kwargs)
            message = _('Raw material "%(name)s" (%(code)s) successfully deleted') % {
                'name': self.object.name, 'code': self.object.code
            }
            messages.success(self.request, message)
            return result
        except ProtectedError:
            message = _('Cannot delete raw material "%(name)s" (%(code)s) since it is in use') % {
                'name': self.object.name, 'code': self.object.code
            }
            messages.error(self.request, message)
            return self.get(request, *args, **kwargs)


class RawMaterialDetail(BaseContextMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'materials.view_rawmaterial'
    model = RawMaterial
