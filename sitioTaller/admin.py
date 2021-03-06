from django.contrib.admin       import AdminSite
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin  import UserAdmin, GroupAdmin
from news.models                import Category, Carousel, New, NewGallery
from news.admin                 import NewAdmin
from contact.models             import Message


class MyAdminSite(AdminSite):
	site_header = 'Administración de \"sitio taller\"'
	site_title = '\"Sitio taller\"'
	site_url = None
	index_title = 'Administrador'

admin_site = MyAdminSite(name='myadmin')
admin_site.register(User, UserAdmin)
admin_site.register(Group, GroupAdmin) 
admin_site.register(Category)
admin_site.register(Carousel)
admin_site.register(New, NewAdmin)
admin_site.register(NewGallery)
admin_site.register(Message)
