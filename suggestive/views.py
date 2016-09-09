from django.core.exceptions import ImproperlyConfigured
from django.db.models import Q
from django.views.generic import View
from django.views.generic.list import MultipleObjectMixin
from django.http import JsonResponse
from django.utils.six import text_type
import operator


class SearchView(MultipleObjectMixin, View):
    """
    This view performs a search and returns its results as json. It is intended to provide
      an autocomplete field for the forms. However, this view will not be mirrored like it
      was in J.A.C.K.F.R.O.S.T. by internal validation mechanisms since those mechanisms
      are not necessarily implementable in a DRY way.

    This view can be used regardless the related UI. This means that this view is compatible
      with jQuery-UI or with Bootstrap-3's TypeAhead (GH: bassjobsen/Bootstrap-3-Typeahead),
      or any autocomplete picking data from an ajax/json request.
    """

    lookup_type = 'icontains'
    search_fields = None
    search_param = 'term'
    search_limit = 25

    label_field = text_type
    label_member = 'label'
    value_field = 'pk'
    value_member = 'value'

    def get_lookup_type(self):
        """
        Returns the lookup type. The returned value should be a valid lookup registered in your
          django project, like "istartswith", "iexact", or "icontains". Please note that starting
          from Django 1.10 the "search" lookup will not be available anymore.

        If you don't need custom per-request behavior, just set the "lookup_type" variable.
        :return:
        """

        return self.lookup_type

    def get_search_fields(self):
        """
        Returns the fields used for the search. At least one field must be specified. in the search.
        Either this method must be overridden or the `search_fields` member must be set.
        :return:
        """

        search_fields = self.search_fields
        if not search_fields:
            raise ImproperlyConfigured(
                "%(cls)s is missing a list of search fields. Define "
                "%(cls)s.search_fields, or override %(cls)s.get_queryset()." % {
                    'cls': self.__class__.__name__
                }
            )
        return search_fields

    def get_search_param(self):
        """
        Returns the http querystring field used for the search. By default this querystring field is 'term'.
        Either this method must be overridden or the `search_fields` member must be changed, but anyway an
          empty value (e.g. None, False) is forbidden.
        :return:
        """

        return self.search_param

    def get_search_limit(self):
        """
        Returns the maximum number of records to show. By default the result is 25.
        Either this method must be overridden or the `search_limit` member must be changed. Any integer
          number is allowed, or None to not apply any limit.
        :return:
        """

        return self.search_limit

    def get_search_queryset(self):
        """
        Gets a filtered-for-search queryset.
        :return:
        """

        queryset = self.get_queryset()
        lookup_type = self.get_lookup_type()
        lookup_fields = ["%s__%s" % (field, lookup_type) for field in self.get_search_fields()]
        term = self.request.GET.get(self.search_param, '')
        search_limit = self.get_search_limit()

        for part in term.split():
            queryset = queryset.filter(reduce(operator.or_, [Q(**{lookup: part}) for lookup in lookup_fields]))

        if search_limit is not None:
            queryset = queryset[:search_limit]

        return queryset

    def get_label_field(self):
        """
        Returns the field to get the (selection) option label from. Default is `str` (python 3) or `unicode` (python 2).
        Allowed return values are a string (interpreted as an attribute) or a callable (accepting one model object).
        Either this method should be overridden or the `label_field` member must be changed.
        :return:
        """

        return self.label_field

    def get_label_member(self):
        """
        Returns the json member to set the (selection) option label to. Default is 'label'.
        Either this method should be overridden or the `label_member` member must be changed.
        :return:
        """

        return self.label_field

    def get_value_field(self):
        """
        Returns the field to get the (selection) option value from. Default is 'pk'.
        Allowed return values are a string (interpreted as an attribute) or a callable (accepting one model object).
        Either this method should be overridden or the `value_field` member must be changed.
        :return:
        """

        return self.value_field

    def get_value_member(self):
        """
        Returns the json member to set the (selection) option value to. Default is 'value'.
        Either this method should be overridden or the `value_member` member must be changed.
        :return:
        """

        return self.value_field

    def get_extra_data(self):
        """
        Override this method to provide extra data to the resulting JSON object.
        :return:
        """

        return {}

    def build_json(self, obj, label_field, label_member, value_field, value_member):
        """
        Builds the json result for a single object.
        :param obj: The model object.
        :param label_field: The field (or callable) to get the label from.
        :param label_member: The json member to set the label to.
        :param value_field: The field (or callable) to get the value from.
        :param value_member: The json member to set the value to.
        :return: a JSON object.
        """

        if callable(label_field):
            label = label_field(obj)
        else:
            label = getattr(obj, label_field)

        if callable(value_field):
            value = value_field(obj)
        else:
            value = getattr(obj, value_field)

        json_value = {value_member: value, label_member: label}
        json_value.update(self.get_extra_data())
        return json_value

    def get(self, request, *args, **kwargs):
        """
        Returns a json response with the contents.
        :param request: The request being processed
        :param args:
        :param kwargs:
        :return:
        """

        label_field = self.get_label_field()
        label_member = self.get_label_member()
        value_field = self.get_value_field()
        value_member = self.get_value_member()
        queryset = self.get_search_queryset()

        return JsonResponse([self.build_json(obj, label_field, label_member, value_field, value_member)
                             for obj in queryset])


def search_view(klass=SearchView, **kwargs):
    """
    Function-style setting -shortcut- for the SearchView.
    :param klass: The class to use as base.
    :param kwargs: Args for the view generation.
    :return:
    """

    if not isinstance(klass, type) or not issubclass(klass, SearchView):
        raise TypeError('Expected a SearchView subclass as the first argument')
    return klass.as_view(**kwargs)
