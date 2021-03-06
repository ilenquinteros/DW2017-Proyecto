# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-27 06:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Noticias', '0002_auto_20170627_0614'),
    ]

    operations = [
        migrations.AddField(
            model_name='comentario',
            name='noticia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Noticias.Noticia'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comentario',
            name='lector',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Noticias.Lector'),
            preserve_default=False,
        ),
    ]
