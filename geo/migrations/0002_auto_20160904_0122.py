# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-09-04 06:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='city',
            name='code',
            field=models.SlugField(help_text='An internal code for the element (10 alphanumeric characters or hyphens/underscores). The code must not repeat on different records', max_length=30, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='city',
            name='enabled',
            field=models.BooleanField(default=True, help_text='When set to False, this element cannot be used anymore when picking these elements as related values in the corresponding fields', verbose_name='Enabled'),
        ),
        migrations.AlterField(
            model_name='city',
            name='name',
            field=models.CharField(help_text='A descriptive text for the element (100 characters)', max_length=100, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='province',
            name='code',
            field=models.SlugField(help_text='An internal code for the element (10 alphanumeric characters or hyphens/underscores). The code must not repeat on different records', max_length=30, unique=True, verbose_name='Code'),
        ),
        migrations.AlterField(
            model_name='province',
            name='enabled',
            field=models.BooleanField(default=True, help_text='When set to False, this element cannot be used anymore when picking these elements as related values in the corresponding fields', verbose_name='Enabled'),
        ),
        migrations.AlterField(
            model_name='province',
            name='name',
            field=models.CharField(help_text='A descriptive text for the element (100 characters)', max_length=100, verbose_name='Name'),
        ),
    ]