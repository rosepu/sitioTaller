import os

from django.conf import settings
from django.db   import models
from io          import BytesIO
from zipfile     import ZipFile


class Category(models.Model):
	name = models.CharField(max_length=100, verbose_name='Nombre Categoria')
	slug = models.SlugField(max_length=100, db_index=True)

	def __str__(self):
		return u'%s' % (self.name)


class New(models.Model):
	TEXT_TYPE = 0
	GALLERY_TYPE = 1
	NOURL_TYPE = 2
	TYPE_CHOICES = (
		(TEXT_TYPE, 'Text'),
		(GALLERY_TYPE, 'Gallery'),
		(NOURL_TYPE, 'NoUrl')
	)

	title    = models.CharField(max_length=100, verbose_name='Titulo') 
	new_type = models.IntegerField(choices=TYPE_CHOICES, default=TEXT_TYPE, verbose_name='Tipo')
	image    = models.ImageField(upload_to = 'img/news')
	body     = models.TextField()
	slug     = models.SlugField(max_length=100, unique=True)
	date     = models.DateTimeField(db_index=True, auto_now_add=True, verbose_name='Fecha')
	category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)

	def __str__(self):
		return u'%s' % (self.title)

	def body_as_list(self):
		return self.body.split('\n')


class NewGallery(models.Model):
	amount     = models.IntegerField(default=-1)
	owner_new  = models.OneToOneField(New, on_delete=models.CASCADE, primary_key=True)
	zip_import = models.FileField(verbose_name='Zip import', blank=True, null=True, upload_to='img/news/zip')

	def __str__(self):
		return u'%s\'s gallery' % (self.owner_new)

	def save(self, *args, **kwargs):
		if (self.owner_new.new_type != New.GALLERY_TYPE):
			return
		super(NewGallery, self).save(*args, **kwargs)
		if self.zip_import:
			zip_file = ZipFile(self.zip_import)
			i_name = 1
			directory_path = os.path.join(settings.MEDIA_ROOT, 'img', 'news', 'gallery', self.owner_new.slug)
			os.makedirs(directory_path)
			for name in zip_file.namelist():
				data = zip_file.read(name)
				try:
					from PIL import Image
					image = Image.open(BytesIO(data))
					image.load()
					image = Image.open(BytesIO(data))
					image.verify()
				except ImportError:
					pass
				except:
					continue
				
				file_name = str(i_name) + '.jpg'
				save_path = os.path.join(directory_path, file_name)
				try:
					image = Image.open(BytesIO(data)).convert('RGB')
					image.save(save_path)
					i_name+=1
				except Exception as e: 
					print(e)
					print('error zip')
			zip_file.close()
			self.zip_import.delete(save=True)
			self.amount = i_name-1
			super(NewGallery, self).save(*args, **kwargs)
