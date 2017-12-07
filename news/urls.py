from django.conf.urls import url
from .                import views

app_name = 'news'
urlpatterns = [
	# ex: /news/
	url(r'^$', views.index, name='index'),
	# ex: /news/slug/
	url(r'^(?P<new_slug>[0-9a-zA-Z]+)/$', views.detail, name='detail'),
	# ex: /news/category/slug/
	url(r'^category/(?P<category_slug>[0-9a-zA-Z]+)/$', views.category_index, name='category'),
]
