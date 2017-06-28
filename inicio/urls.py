from django.conf.urls import patterns, include urls

urlpatterns = patterns('',

	url(r'^$', 'django.contrib.auth.views.login',
		{'template_name:templates/login_registro.html'}, name='login'),
		url(r'^$', 'django.contrib.auth.views.logout_then_login', name='logout'),	

)