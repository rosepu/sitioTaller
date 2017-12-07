from django.http      import HttpResponse
from django.shortcuts import get_object_or_404,render
from .models          import New, NewGallery, Carousel

def index(request):
	new_list = New.objects.order_by('-date')
	context = {
		'new_list': new_list
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
