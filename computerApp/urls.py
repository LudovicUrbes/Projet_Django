from django.urls import path
from computerApp import views

urlpatterns = [
	path ('start.html', views.start, name="start"),
	path ('index.html' , views.index , name ='index'),
	path ('visualisation.html', views.visualisation, name="visualisation"),
	path ('contact.html', views.contact, name="contact"),
	path ('machines/' , views.machine_list_view, name='machines'),
	path ('machine/<pk>' , views.machine_detail_view, name='machine-detail'),
	path ('add-machine' , views.machine_add_form ,name='add-machine'),
]