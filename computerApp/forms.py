from django.urls import path
from django import forms
from django.core.exceptions import ValidationError

class AddMachineForm (forms.Form) :

    nom = forms.CharField (required =True , label ='Nom de la machine')

    def clean_nom ( self ):
        data = self.cleaned_data ["nom"]

        if len( data ) != 6:
            raise ValidationError ((" Erreur de format pour le champ nom "))

        return data

class AddEmployeForm (forms.Form) :

    nom = forms.CharField (required =True , label ='Nom de l\'employé')
    prenom = forms.CharField (required =True , label ='Prénom de l\'employé')
    def clean_nom ( self ):
        data = self.cleaned_data ["nom"]
        data_2 = self.cleaned_data ["prenom"]

        if len( data ) != 15:
            raise ValidationError ((" Erreur de format pour le champ nom "))

        if len( data_2 ) != 15:
            raise ValidationError ((" Erreur de format pour le champ prénom "))

        return data, data_2


