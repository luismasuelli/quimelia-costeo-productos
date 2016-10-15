from django.contrib import messages
from django.core.urlresolvers import reverse_lazy, reverse
from django.db.models import Count, ProtectedError
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, View
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.utils.translation import ugettext_lazy as _
from support.search.views import SearchListView
from main.views import BaseContextMixin
from .models import Entity, ClientAccount, ServiceArea
from .forms import EntityForm, ClientAccountForm


class EntitiesList(BaseContextMixin, PermissionRequiredMixin, SearchListView):
    permission_required = 'contacts.list_entity'
    queryset = Entity.objects.annotate(client_accounts_count=Count('client_accounts'))
    search_fields = ('identification', 'name', 'address', 'city__name')
    model = Entity


class EntityCreate(BaseContextMixin, PermissionRequiredMixin, SuccessMessageMixin, CreateView):
    permission_required = 'contacts.add_entity'
    form_class = EntityForm
    model = Entity
    success_url = reverse_lazy('contacts:entities-list')

    def get_success_message(self, cleaned_data):
        return _('Entity "%(name)s" (%(identification)s) successfully created') % {
            'name': self.object.name, 'identification': self.object.identification
        }


class EntityUpdate(BaseContextMixin, PermissionRequiredMixin, SuccessMessageMixin, UpdateView):
    permission_required = 'contacts.change_entity'
    form_class = EntityForm
    model = Entity

    def get_success_message(self, cleaned_data):
        return _('Entity "%(name)s" (%(identification)s) successfully updated') % {
            'name': self.object.name, 'identification': self.object.identification
        }

    def get_success_url(self):
        return reverse('contacts:entities-update', kwargs={'pk': self.object.pk})


class EntityDelete(BaseContextMixin, PermissionRequiredMixin, DeleteView):
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


class EntityDetail(BaseContextMixin, PermissionRequiredMixin, DetailView):
    permission_required = 'contacts.view_entity'
    model = Entity


class ClientAccountView(BaseContextMixin, View):

    def get_parent_object(self):
        if not getattr(self, '_parent_object', None):
            self._parent_object = Entity.objects.get(pk=self.kwargs['pk'])
        return self._parent_object

    def get_queryset(self):
        return ClientAccount.objects.filter(entity=self.get_parent_object())

    def get_context_data(self, **kwargs):
        context_data = super(ClientAccountView, self).get_context_data(**kwargs)
        context_data.update({
            'parent': self.get_parent_object()
        })
        return context_data


class ClientAccountCreate(PermissionRequiredMixin, SuccessMessageMixin, CreateView, ClientAccountView):
    permission_required = 'contacts.add_clientaccount'
    form_class = ClientAccountForm
    model = ClientAccount
    pk_url_kwarg = 'ca_pk'

    def get_success_url(self):
        return reverse('contacts:entities-detail', kwargs={'pk': self.kwargs['pk']})

    def get_success_message(self, cleaned_data):
        parent = self.get_parent_object()

        return _('Client account in service area "%(sname)s" for entity "%(name)s" (%(identification)s) '
                 'successfully created') % {
            'sname': self.object.service_area.name, 'name': parent.name, 'identification': parent.identification
        }

    def get_form(self, form_class=None):
        """
        The form is instantiated as usual (with the instance to edit and perhaps the data), with the
          specified form_class (if specified). Then, we restrict the available service_area objects since
          they cannot repeat for the same entity.

        Since the instance is new, we must give it the parent entity. This will help the instance to
          validate correctly later.
        :param form_class: The class to instantiate the form with.
        :return: The created form.
        """

        form = super(ClientAccountCreate, self).get_form(form_class)
        parent = self.get_parent_object()
        form.instance.entity = parent
        pks = parent.client_accounts.values_list('service_area__pk', flat=True)
        form.fields['service_area'].queryset = ServiceArea.objects.filter(enabled=True).exclude(pk__in=pks)
        return form


class ClientAccountUpdate(PermissionRequiredMixin, SuccessMessageMixin, UpdateView, ClientAccountView):
    permission_required = 'contacts.change_clientaccount'
    form_class = ClientAccountForm
    model = ClientAccount
    pk_url_kwarg = 'ca_pk'

    def get_success_url(self):
        return reverse('contacts:client-accounts-update', kwargs={'pk': self.kwargs['pk'], 'ca_pk': self.object.pk})

    def get_success_message(self, cleaned_data):
        parent = self.get_parent_object()
        return _('Client account in service area "%(sname)s" for entity "%(name)s" (%(identification)s) '
                 'successfully created') % {
            'sname': self.object.service_area.name, 'name': parent.name, 'identification': parent.identification
        }

    def get_form(self, form_class=None):
        """
        The form is instantiated as usual (with the instance to edit and perhaps the data), with the
          specified form_class (if specified). Then, we restrict the available service_area objects since
          they cannot repeat for the same entity.
        :param form_class: The class to instantiate the form with.
        :return: The created form.
        """

        form = super(ClientAccountUpdate, self).get_form(form_class)
        pks = self.get_parent_object().client_accounts.exclude(pk=form.instance.pk).values_list('service_area__pk', flat=True)
        form.fields['service_area'].queryset = ServiceArea.objects.filter(enabled=True).exclude(pk__in=pks)
        return form


class ClientAccountDelete(PermissionRequiredMixin, DeleteView, ClientAccountView):
    permission_required = 'contacts.delete_clientaccount'
    model = ClientAccount
    pk_url_kwarg = 'ca_pk'

    def get_success_url(self):
        return reverse('contacts:entities-detail', kwargs={'pk': self.kwargs['pk']})

    def post(self, request, *args, **kwargs):
        try:
            result = self.delete(request, *args, **kwargs)
            message = _('Account for service area "%(name)s" successfully deleted') % {
                'name': self.object.service_area.name,
            }
            messages.success(self.request, message)
            return result
        except ProtectedError:
            message = _('Cannot delete account for service area "%(name)s" since it is in use') % {
                'name': self.object.service_area.name,
            }
            messages.error(self.request, message)
            return self.get(request, *args, **kwargs)


class ClientAccountDetail(PermissionRequiredMixin, DetailView, ClientAccountView):
    permission_required = 'contacts.view_clientaccount'
    model = ClientAccount
    pk_url_kwarg = 'ca_pk'
