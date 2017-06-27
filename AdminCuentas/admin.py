# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from AdminCuentas.models import Editor, Admin, Categoria

class AdminAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'username','email','fecha_creacion')
    #list_filter = ('owner','active')
    search_fields = ('nombre','username',)

class EditorAdmin(admin.ModelAdmin):
    list_display = ('nombre','username','email', 'fecha_creacion')
    search_fields = ('nombre','username',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre_categoria', 'fecha_creacion')
    #list_filter = ('owner','active')
    search_fields = ('nombre_categoria',)

admin.site.register(Admin, AdminAdmin)
admin.site.register(Editor, EditorAdmin)
admin.site.register(Categoria, CategoriaAdmin)

