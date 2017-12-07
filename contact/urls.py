from django.conf.urls import url
from .                import views

app_name = 'contact'
urlpatterns = [
	# ex: /contact/
	url(r'^$', views.index, name='index'),
]
