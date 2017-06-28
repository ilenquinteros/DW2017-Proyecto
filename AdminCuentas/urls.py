from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^editor/$', views.editorList.as_view(), name='editor'),
    url(r'^cuentas/$', views.cuentasList.as_view(), name='cuentas'),
    url(r'^editor/nueva_categoria$', views.categoriaCreate.as_view(), name='addCat'),
    url(r'^editor/editar_categoria/(?P<pk>[0-9]+)/$', views.categoriaUpdate.as_view(), name='editCat'),
    url(r'^editor/eliminar_categoria/(?P<pk>[0-9]+)/$', views.categoriaDelete.as_view(), name='delCat'),
    url(r'^editor/nueva_noticia$', views.noticiaCreate.as_view(), name='addNot'),
    url(r'^editor/editar_noticia/(?P<pk>[0-9]+)/$', views.noticiaUpdate.as_view(), name='editNot'),
    url(r'^editor/eliminar_noticia/(?P<pk>[0-9]+)/$', views.noticiaDelete.as_view(), name='delNot'),
]