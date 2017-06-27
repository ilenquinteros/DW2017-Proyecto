# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from Noticias.models import Noticia, Comentario, Lector

class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo_noticia','autor','categoria', 'fecha_creacion')
    search_fields = ('titulo_noticia',)

class LectorAdmin(admin.ModelAdmin):
    list_display = ('username', 'email','fecha_creacion')
    #list_filter = ('owner','active')
    search_fields = ('username',)

class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('lector', 'noticia','fecha_creacion')
    #list_filter = ('owner','active')
    search_fields = ('noticia','lector',)

admin.site.register(Noticia, NoticiaAdmin)
admin.site.register(Lector, LectorAdmin)
admin.site.register(Comentario, ComentarioAdmin)