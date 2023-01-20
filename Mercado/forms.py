from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class ofertaform(forms.Form):
    cultivo=forms.CharField(max_length=50)
    volumen=forms.IntegerField()
    cosecha=forms.CharField(max_length=50)
    

class demandaform(forms.Form):
    cultivo=forms.CharField(max_length=50)
    volumen=forms.IntegerField()
    cosecha=forms.CharField(max_length=50)