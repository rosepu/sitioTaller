from django.db import models

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
	new_type = models.IntegerField(choices=TYPE_CHOICES, default=TEXT_TYPE)
	image    = models.ImageField(upload_to = "img/news")
	body     = models.TextField()
	slug     = models.SlugField(max_length=100, unique=True)
	date     = models.DateTimeField(db_index=True, auto_now_add=True)
	category = models.ForeignKey(Category, on_delete=models.PROTECT, blank=True, null=True)

	def body_as_list(self):
		return self.body.split('\n')

class NewGallery(models.Model):
	amount    = models.IntegerField(default=-1)
	owner_new = models.OneToOneField(New, on_delete=models.CASCADE, primary_key=True)

	def __str__(self):
		return 

	def __unicode__(self):
		return 
