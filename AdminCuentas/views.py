# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def editor(request):
	return render(request, 'editor.html')

def cuentas(request):
	return render(request, 'admin_cuentas.html')

def login(request):
	return render(request, 'login_registro.html')