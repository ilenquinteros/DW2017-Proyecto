from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^editor/$', views.editor, name='editor'),
    url(r'^cuentas/$', views.cuentas, name='cuentas'),
    url(r'^login/$', views.login, name='login'),
]