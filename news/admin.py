from django.contrib import admin
from .models import New, Category, NewGallery, Carousel


class GalleryInline(admin.StackedInline):
	model = NewGallery
	extra = 1

class NewAdmin(admin.ModelAdmin):
	list_display = ('title', 'date', 'new_type')
	inlines = []
	
	def get_form(self, request, obj=None, **kwargs):
		if (obj == None or obj.new_type ==  New.GALLERY_TYPE): 
			self.inlines = [GalleryInline]
		return super(NewAdmin, self).get_form(request, obj, **kwargs)

admin.site.register(New, NewAdmin)
admin.site.register(Category)
admin.site.register(NewGallery)
admin.site.register(Carousel)
