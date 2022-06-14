from django.contrib import admin

# Register your models here.

from .models import Machine
from .models import Employe

admin.site.register(Machine)
admin.site.register(Employe)