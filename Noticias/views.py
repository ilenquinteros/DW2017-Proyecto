# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.views.generic import ListView
from models import Noticia

def home(request):
	return render(request, 'home.html')

def categoria(request):
	return render(request, 'categorias.html')

def noticia(request):
	return render(request, 'noticia.html')

class homeList (ListView):
	model = Noticia
	template_name = 'home.html'