from django.forms import Form
from django.forms.fields import CharField


form_classes_by_names = {}
def search_form_factory(field_name='term', label='Search'):
    try:
        return form_classes_by_names[field_name]
    except KeyError:
        form_classes_by_names[field_name] = type('SearchForm', (Form,), {field_name: CharField(label=label,
                                                                                               required=False)})
        return form_classes_by_names[field_name]
