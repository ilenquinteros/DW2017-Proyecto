# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sorl.thumbnail import ImageField
from django.db import models
from AdminCuentas.models import Categoria, Editor

class Noticia(models.Model):
    titulo_noticia = models.CharField(max_length=100)
    contenido = models.TextField()
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    autor = models.ForeignKey(Editor)
    imagen = models.ImageField(upload_to='images')
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.titulo_noticia

class Lector(models.Model):
    username = models.CharField(max_length=100)
    contrasena = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    # sort_order = models.IntegerField(default=0)
    # status = models.BooleanField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.username

class Comentario(models.Model):
    lector = models.ForeignKey(Lector)
    noticia = models.ForeignKey(Noticia)
    contenido = models.TextField()
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True)
    # sort_order = models.IntegerField(default=0)
    # status = models.BooleanField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)