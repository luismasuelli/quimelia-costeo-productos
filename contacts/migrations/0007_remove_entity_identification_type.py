# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-10-01 23:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0006_auto_20161001_1802'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entity',
            name='identification_type',
        ),
    ]