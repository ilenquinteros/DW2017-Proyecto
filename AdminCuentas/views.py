# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from forms import CategoriaForm
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from Noticias.models import Noticia
from models import Editor, Categoria


def login(request):
	return render(request, 'login_registro.html')

class cuentasList(ListView):
	template_name = 'admin_cuentas.html'
	model = Editor

class editorList(ListView):
	template_name = 'editor.html'
	def get_queryset(self):
		categorias = Categoria.objects.all()
		noticias = Noticia.objects.all()
		result = {'noticias': noticias, 'categorias': categorias}
		return result





class categoriaCreate(CreateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'edicion_categoria.html' 	
	success_url = reverse_lazy('editor')

class categoriaUpdate(UpdateView):
	model = Categoria
	form_class = CategoriaForm
	template_name = 'edicion_categoria.html' 	
	success_url = reverse_lazy('editor')

class categoriaDelete(DeleteView):
	model = Categoria
	template_name = 'eliminar_categoria.html' 	
	success_url = reverse_lazy('editor')