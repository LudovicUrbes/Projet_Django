from django.shortcuts import get_object_or_404, render, redirect
from computerApp.models import Machine
from computerApp.forms import AddMachineForm

# Create your views here.

""""
from django.http import HttpResponse
from django.shortcuts import render
from matplotlib.style import context

def index(request):
	context = {
			'machines': machines,
			"form" : form
}
	return render(request, 'index.html', context=context)

from computerApp.models import Machine

machines = Machine.objects.all()
machines = Machine.objects.filter(id=1)
machines = Machine.objects.order_by('id')
machines = Machine.objects.filter(bureau.numero='001')
"""

def index (request) :
	return render (request, 'index.html', {})

def start (request) :
	return render (request, 'start.html', {})

def contact (request) :
	return render (request, 'contact.html', {})

def visualisation (request) :
	return render (request, 'visualisation.html', {})

def machine_list_view (request) :
	machines = Machine.objects.all()
	context = {'machines': machines}
	return render(request, 'computerapp/machine_list.html',context)	

def machine_detail_view(request , pk):
	machine = get_object_or_404(Machine, id=pk)
	context={'machine': machine}
	return render(request, 'computerapp/machine_detail.html', context)

def machine_add_form(request):
	if request.method == 'POST':
		form = AddMachineForm(request.POST or None)
		if form.is_valid():
			new_machine = Machine(nom=form.cleaned_data['nom'])
			new_machine.save()
			return redirect('machines')
	else :
		form = AddMachineForm()
		context = {'form' : form}
		return render(request,
	 	 'computerapp/machine_add.html',context)