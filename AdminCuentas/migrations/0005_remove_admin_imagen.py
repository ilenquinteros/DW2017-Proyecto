# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 02:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminCuentas', '0004_editor_administrador'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='imagen',
        ),
    ]
