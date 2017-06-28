# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from sorl.thumbnail import ImageField
from django.db import models

class Admin(models.Model):
	nombre = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	contrasena = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.username

class Editor(models.Model):
	nombre = models.CharField(max_length=100)
	username = models.CharField(max_length=100)
	contrasena = models.CharField(max_length=100)
	email = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='images',blank=True,null=True)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	administrador = models.ForeignKey(Admin, null=True, blank=True, on_delete = models.CASCADE)
	# status = models.BooleanField()
	def __str__(self):
		return self.username

class Categoria(models.Model):
	nombre_categoria = models.CharField(max_length=100)
	fecha_creacion = models.DateTimeField(auto_now_add=True)
	fecha_modificacion = models.DateTimeField(auto_now=True)
	# status = models.BooleanField()

	def __str__(self):
		return self.nombre_categoria        
