from django.conf.urls import include, url
from . import views
import AdminCuentas

urlpatterns = [
    url(r'^home/$', views.homeList.as_view(), name='home'),
    # url(r'^categoria/$', views.categoria, name='categoria'),
	# url(r'^noticia/$', views.noticia, name='noticia'),
	url(r'^categoria/(?P<id_categoria>\d+)/$', views.categoriasList.as_view(), name='categoria'),
	url(r'^noticia/(?P<id_noticia>\d+)/$', views.noticiaList.as_view(), name='noticia'),
	url(r'^edit/', include('AdminCuentas.urls')),
]