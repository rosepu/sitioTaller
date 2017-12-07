from django.http      import HttpResponse
from django.shortcuts import get_object_or_404,render
from .models          import New, NewGallery, Carousel, Category

def index(request):
	new_list = New.objects.order_by('-date')
	category_list = Category.objects.order_by('name')
	context = {
		'new_list': new_list,
		'category_list': category_list,
	}
	return render(request, 'news/index.html', context)

def detail(request, new_slug):
	new_detail = get_object_or_404(New, slug=new_slug)
	if (new_detail.new_type == New.GALLERY_TYPE):
		gallery = get_object_or_404(NewGallery, owner_new=new_detail)
		context = {
			'new': new_detail,
			'gallery': gallery,
			'range': range(1, gallery.amount+1)
		}
	else:
		context = {
			'new': new_detail,
		}
	return render(request, 'news/detail.html', context)

def home(request):
	latest_new_list = New.objects.order_by('-date')[:6]
	carousel_home = Carousel.objects.order_by('poss')
	context = {
		'latest_new_list': latest_new_list,
		'carousel': carousel_home,
	}
	return render(request, 'news/home.html', context)

def category_index(request, category_slug):
	category_item = Category.objects.get(slug=category_slug)
	new_list = New.objects.filter(category=category_item).order_by('-date')
	category_list = Category.objects.order_by('name')
	context = {
		'new_list': new_list,
		'category_list': category_list,
	}
	return render(request, 'news/index.html', context)