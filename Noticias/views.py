# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import ListView
from models import Noticia, Comentario

class noticiaList(ListView):
	template_name = 'noticia.html'
	def get_queryset(self):
		id_noticia = self.kwargs['id_noticia']
		comentarios = Comentario.objects.filter(noticia = int(id_noticia)).order_by('-fecha_creacion')
		noticia = Noticia.objects.filter(id = int(id_noticia)).order_by('-fecha_creacion')
		result = {'noticiaDetalle': noticia, 'comentarioDetalle': comentarios}
		return result

class categoriasList(ListView):
	template_name = 'categorias.html'
	def get_queryset(self):
		id_categoria = self.kwargs['id_categoria']
		Noticia.objects.filter(categoria = int(id_categoria)).order_by('-fecha_creacion')
		return 

class homeList (ListView):
	model = Noticia
	template_name = 'home.html'