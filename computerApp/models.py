from platform import machine
import re
from wsgiref.util import request_uri
from django.db import models
from regex import F
import requests
from datetime import datetime
from django.contrib.auth.models import User

# Create your models here.

class Machine(models.Model):
    TYPE = (
        ('PC', ('PC - Run windows ')) ,
        ('Mac', ( ' MAc - Run MacOS ')) ,
        ('Serveur', ('Serveur - Simple Server to deploy virtual machines')),
        ('Switch', ('Switch - To maintains and connect servers')),
    )

    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=20)
    maintenanceDate = models.DateField(default = datetime.now())
    mach = models.CharField(max_length=32, choices=TYPE, default='PC')

class Employe(models.Model):
    TYPE = (
        ('Employé', ('Employé')),
        ('Secrétaire', ('Secrétaire')),
        ('Comptable', ('Comptable')),
        ('Technicien', ('Technicien')),
        ('Chef de projet', ('Chef de projet')),
        ('Chef d\'entreprise', ('Chef d\'entreprise'))
    )
    id = models.AutoField(primary_key=True, editable=False)
    nom = models.CharField(max_length=20)
    prenom = models.CharField(max_length=20)
    mach = models.CharField(max_length=32, choices=TYPE, default='Employé')
    
"""
    id = models.AutoField(
                    primary_key=True,
                    editable=False)
    nom = models.CharField(
                max_length=200)

def __str__ (self):
    return str (self.id) + "->" + self.nom

def get_name(self):
    return str(self.id) + " " + self.nom
"""

"""
from computerApp.models import Machine

class createMachineForm(forms.Form):
    nom = forms.CharField(
        label="Nom de la machine"
    )

    def clean_nom(self):
        data = self.cleaned_data["nom"]
        if len(data) != 6:
            raise ValidationError(_("Erreur de format pour le champs 'nom'"))
        return data

from django.shortcuts import redirect
from computerApp.forms import createMachineForm
from computerApp.models import Machine, Bureau

form = createMachineForm(request.POST or None)

if request.method == "POST":
    if form.is_valid():
        new_machine=Machine(
                nom=form.cleaned_data["nom"]
            )
        machine = Machine.objects.order_by('-id')[0]
        machine.bureau = new_bureau
        machine.save()
        
        new_machine.save()

            return redirect(index)

form = createBureauForm(request.POST or None)
if request.method == "POST":
    if form.is_valid():
        new_bureau=Bureau(
                numero=form.cleaned_data["numéro"]
            )
            new_bureau.save()
"""