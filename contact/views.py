from django.http      import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from django.http.response   import HttpResponseRedirect
from .modelFroms            import ContacForm


def index(request):
	data = {}
	data['titulo'] = 'Formulario de Contacto'
	data['form'] = ContacForm(data=request.POST or None)

	if request.method == 'POST':
		if data['form'].is_valid():
			data['form'].save()
			return HttpResponseRedirect(reverse('contact:index'))

	return render(request, 'contact/index.html', data)
