# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-03-11 21:14
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('materials', '0003_auto_20170115_2317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Label',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Date and time of record creation', verbose_name='Creation Date')),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Date and time of last record update', verbose_name='Update Date')),
                ('name', models.CharField(help_text='A descriptive text for the element (100 characters)', max_length=100, verbose_name='Name')),
                ('code', models.SlugField(help_text='An internal code for the element (10 alphanumeric characters or hyphens/underscores). The code must not repeat on different records', max_length=30, unique=True, verbose_name='Code')),
                ('enabled', models.BooleanField(default=True, help_text='When set to False, this element cannot be used anymore when picking these elements as related values in the corresponding fields', verbose_name='Enabled')),
                ('notes', models.TextField(blank=True, default=b'', help_text='Optional internal notes to add to the element. Usually they determine the meaning of the element.', verbose_name='Additional Notes')),
                ('price', models.DecimalField(decimal_places=3, max_digits=7, validators=[django.core.validators.MinValueValidator(0.001)], verbose_name='Price')),
            ],
            options={
                'verbose_name': 'Label',
                'verbose_name_plural': 'Labels',
                'permissions': (('list_label', 'Can list Label'), ('view_label', 'Can view Label')),
            },
        ),
    ]