from django.shortcuts import get_object_or_404, render, redirect
from computerApp.models import Employe, Machine
from computerApp.forms import AddEmployeForm, AddMachineForm

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

def employe_list_view (request) :
	employes = Employe.objects.all()
	context = {'employes': employes}
	return render(request, 'computerapp/employe_list.html',context)	

def employe_detail_view(request , pk):
	employe = get_object_or_404(Employe, id=pk)
	context={'employe': employe}
	return render(request, 'computerapp/employe_detail.html', context)


def employe_add_form(request):
	if request.method == 'POST':
		form = AddEmployeForm(request.POST or None)
		if form.is_valid():
			new_employe = Employe(nom=form.cleaned_data['nom'])
			new_employe_2 = Employe(prenom=form.cleaned_data['prenom'])
			new_employe.save()
			new_employe_2.save()
			return redirect('employes')
	else :
		form = AddEmployeForm()
		context = {'form' : form}
		return render(request,'computerapp/employe_add.html',context)