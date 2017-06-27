# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

def home(request):
	return render(request, 'home.html')

def categoria(request):
	return render(request, 'categoria.html')

def noticia(request):
	return render(request, 'noticia.html')
