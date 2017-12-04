from django.http      import HttpResponse
from django.shortcuts import get_object_or_404,render
from .models          import New

def index(request):
	new_list = New.objects.order_by('-date')
	context = {
		'new_list': new_list
	}
	return render(request, 'news/index.html', context)

def detail(request, new_slug):
	new_detail = get_object_or_404(New, slug=new_slug)
	body = new_detail.body.split('\n')
	context = {
		'new': new_detail,
	}
	return render(request, 'news/detail.html', context)

def home(request):
	latest_new_list = New.objects.order_by('-date')[:6]
	context = {
		'latest_new_list': latest_new_list
	}
	return render(request, 'news/home.html', context)
