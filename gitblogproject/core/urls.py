from django.conf.urls import url, include
from core.views import home, lista
from django.urls import path

urlpatterns = [
	url(r'^$', lista),
	path('padrao/', home),
	path('accounts/', include('django.contrib.auth.urls')),
]
