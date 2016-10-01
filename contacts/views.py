from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.contrib.auth.mixins import PermissionRequiredMixin
from support.search.views import SearchListView
from .models import Entity, ClientAccount


class EntitiesList(PermissionRequiredMixin, SearchListView):
    permission_required = 'contacts.list_entity'
    search_fields = ('identification', 'name', 'address', 'city__name')
    model = Entity


class EntityCreate(PermissionRequiredMixin, CreateView):
    permission_required = 'contacts.add_entity'
    model = Entity


class EntityUpdate(PermissionRequiredMixin, UpdateView):
    permission_required = 'contacts.change_entity'
    model = Entity


class EntityDelete(PermissionRequiredMixin, DeleteView):
    permission_required = 'contacts.delete_entity'
    model = Entity


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
