from django.contrib import messages
from django.core.urlresolvers import reverse_lazy
from django.db.models import Count, ProtectedError
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext_lazy as _
from support.search.views import SearchListView
from .models import Entity, ClientAccount
from .forms import EntityForm


class EntitiesList(PermissionRequiredMixin, SearchListView):
    permission_required = 'contacts.list_entity'
    queryset = Entity.objects.annotate(client_accounts_count=Count('client_accounts'))
    search_fields = ('identification', 'name', 'address', 'city__name')
    model = Entity


class EntityCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'contacts.add_entity'
    form_class = EntityForm
    model = Entity
    success_url = reverse_lazy('contacts:entities-list')

    def get_success_message(self, cleaned_data):
        return _('Entity "%(name)s" (%(identification)s) successfully created') % {
            'name': self.object.name, 'identification': self.object.identification
        }


class EntityUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'contacts.change_entity'
    form_class = EntityForm
    model = Entity

    def get_success_message(self, cleaned_data):
        return _('Entity "%(name)s" (%(identification)s) successfully updated') % {
            'name': self.object.name, 'identification': self.object.identification
        }

    def get_success_url(self):
        return reverse_lazy('contacts:entities-update', kwargs={'pk': self.object.pk})


class EntityDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'contacts.delete_entity'
    model = Entity
    success_url = reverse_lazy('contacts:entities-list')

    def post(self, request, *args, **kwargs):
        try:
            result = self.delete(request, *args, **kwargs)
            message = _('Entity "%(name)s" (%(identification)s) successfully deleted') % {
                'name': self.object.name, 'identification': self.object.identification
            }
            messages.success(self.request, message)
            return result
        except ProtectedError:
            message = _('Cannot delete entity "%(name)s" (%(identification)s) since it is in use') % {
                'name': self.object.name, 'identification': self.object.identification
            }
            messages.error(self.request, message)
            return self.get(request, *args, **kwargs)


class EntityDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'contacts.view_entity'
    model = Entity


class ClientAccountsList(PermissionRequiredMixin, SearchListView):
    permission_required = 'contacts.list_clientaccount'
    search_fields = ('entity__identification', 'entity__name', 'entity__address', 'entity__city__name',
                     'service_area__name')
    model = ClientAccount


class ClientAccountCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'contacts.add_clientaccount'
    model = ClientAccount


class ClientAccountUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'contacts.change_clientaccount'
    model = ClientAccount


class ClientAccountDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'contacts.delete_clientaccount'
    model = ClientAccount


class ClientAccountDetail(PermissionRequiredMixin, DetailView):
    permission_required = 'contacts.view_clientaccount'
    model = ClientAccount


# Service Areas will be created on management.
