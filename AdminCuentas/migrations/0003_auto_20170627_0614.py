# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 06:14
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AdminCuentas', '0002_auto_20170627_0609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='admin',
            name='editores',
        ),
        migrations.RemoveField(
            model_name='editor',
            name='noticias',
        ),
    ]
