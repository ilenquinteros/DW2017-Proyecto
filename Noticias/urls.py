from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^home/$', views.homeList.as_view(), name='home'),
    url(r'^categoria/$', views.categoria, name='categoria'),
	url(r'^noticia/$', views.noticia, name='noticia'),
#     url(r'^categoria/(?P<category_id>\d+)/$', views.categoria, name='categoria'),
#     url(r'^noticia/(?P<noticia_id>\d+)/$', views.noticia, name='noticia'),
]