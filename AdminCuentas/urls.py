from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^editor/$', views.editorList.as_view(), name='editor'),
    url(r'^cuentas/$', views.cuentasList.as_view(), name='cuentas'),
    url(r'^editor/nueva_Categoria$', views.categoriaCreate.as_view(), name='addCat'),
    url(r'^editor/editar_Categoria/(?P<pk>[0-9]+)/$', views.categoriaUpdate.as_view(), name='editCat'),
    url(r'^editor/eliminar_Categoria/(?P<pk>[0-9]+)/$', views.categoriaDelete.as_view(), name='delCat'),
    url(r'^login/$', views.login, name='login'),
]