from django.urls import path
from computerApp import views

urlpatterns = [
	path ('' , views.index , name ='index'),
	path ('machines/' , views.machine_list_view, name='machines'),
	path ('machine/<pk>' , views.machine_detail_view, name='machine_detail'),
	path ('add-machine' , views.machine_add_form ,name='add_machine'),
]