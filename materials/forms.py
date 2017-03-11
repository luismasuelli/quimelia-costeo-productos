from django.forms.models import modelform_factory
from django.forms.widgets import CheckboxInput
from .models import WorkForce, RawMaterial, Packaging, Label

PackagingForm = modelform_factory(Packaging, fields=('name', 'code', 'price', 'enabled', 'notes'),
                                  widgets={'enabled': CheckboxInput(attrs={'data-toggle': 'toggle'})})
LabelForm = modelform_factory(Label, fields=('name', 'code', 'price', 'enabled', 'notes'),
                              widgets={'enabled': CheckboxInput(attrs={'data-toggle': 'toggle'})})
RawMaterialForm = modelform_factory(RawMaterial, fields=('name', 'code', 'kg_price', 'special', 'enabled', 'notes'),
                                    widgets={'enabled': CheckboxInput(attrs={'data-toggle': 'toggle'})})
WorkForceForm = modelform_factory(WorkForce, fields=('name', 'code', 'hourly_price', 'enabled', 'notes'),
                                  widgets={'enabled': CheckboxInput(attrs={'data-toggle': 'toggle'})})
