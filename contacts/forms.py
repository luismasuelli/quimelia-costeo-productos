from django.forms.models import modelform_factory
from django.forms.widgets import CheckboxInput
from .models import Entity, ClientAccount


EntityForm = modelform_factory(Entity, fields=('identification', 'identification_type', 'identification_country',
                                               'name', 'address', 'city', 'provider'),
                               widgets={'provider': CheckboxInput(attrs={'data-toggle': 'toggle'})})
