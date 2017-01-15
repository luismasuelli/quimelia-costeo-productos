# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-04 06:22
from __future__ import unicode_literals

import catalog.fields
import support.validators.regex
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('geo', '0002_auto_20160904_0122'),
    ]

    operations = [
        migrations.CreateModel(
            name='ClientAccount',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Date and time of record creation', verbose_name='Creation Date')),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Date and time of last record update', verbose_name='Update Date')),
            ],
            options={
                'verbose_name': 'Client Account',
                'verbose_name_plural': 'Client Account',
            },
        ),
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Date and time of record creation', verbose_name='Creation Date')),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Date and time of last record update', verbose_name='Update Date')),
                ('identification', models.CharField(max_length=13, unique=True, validators=[django.core.validators.RegexValidator(b'^\\d*$')], verbose_name='Identification')),
                ('identification_type', models.PositiveSmallIntegerField(choices=[(1, 'Citizen ID'), (2, 'Passport')])),
                ('name', models.CharField(max_length=70, validators=[support.validators.regex.NameRegexValidator(mode=3)], verbose_name='Nombre')),
                ('address', models.CharField(max_length=128, verbose_name='Address')),
                ('city', catalog.fields.CatalogFK(on_delete=django.db.models.deletion.CASCADE, to='geo.City', to_field=b'code', verbose_name='Ciudad')),
            ],
            options={
                'verbose_name': 'Entity',
                'verbose_name_plural': 'Entities',
            },
        ),
        migrations.CreateModel(
            name='ServiceArea',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Date and time of record creation', verbose_name='Creation Date')),
                ('updated_on', models.DateTimeField(default=django.utils.timezone.now, editable=False, help_text='Date and time of last record update', verbose_name='Update Date')),
                ('name', models.CharField(help_text='A descriptive text for the element (100 characters)', max_length=100, verbose_name='Name')),
                ('code', models.SlugField(help_text='An internal code for the element (10 alphanumeric characters or hyphens/underscores). The code must not repeat on different records', max_length=30, unique=True, verbose_name='Code')),
                ('enabled', models.BooleanField(default=True, help_text='When set to False, this element cannot be used anymore when picking these elements as related values in the corresponding fields', verbose_name='Enabled')),
                ('notes', models.TextField(blank=True, default=b'', help_text='Optional internal notes to add to the element. Usually they determine the meaning of the element.', verbose_name='Additional Notes')),
            ],
            options={
                'verbose_name': 'Service Area',
                'verbose_name_plural': 'Service Areas',
            },
        ),
        migrations.AddField(
            model_name='clientaccount',
            name='entity',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contacts.Entity', verbose_name='Entity'),
        ),
        migrations.AddField(
            model_name='clientaccount',
            name='service_area',
            field=catalog.fields.CatalogFK(on_delete=django.db.models.deletion.PROTECT, to='contacts.ServiceArea', to_field=b'code', verbose_name='Service Area'),
        ),
        migrations.AlterUniqueTogether(
            name='clientaccount',
            unique_together=set([('service_area', 'entity')]),
        ),
    ]
