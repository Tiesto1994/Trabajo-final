from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import Template, loader
from Mercado.forms import *
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 
# Create your views here.


@login_required
def ofertaformulario (request):

    if request.method=="POST":
        form=ofertaform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data

            cultivo1=informacion["cultivo"]
            volumen1=informacion["volumen"]
            cosecha1=informacion["cosecha"]
            
            gran_compras=oferta(cultivo=cultivo1,volumen=volumen1,cosecha=cosecha1)
            gran_compras.save()
            return render(request,"MVT_app/inicio.html", {"mensaje":"oferta cargada correctamente"})
    else:
        formulario=ofertaform()


    return render(request,"MVT_app/comprasformulario.html", {"form":formulario})
@login_required
def demandaformulario (request):

    if request.method=="POST":
        form=demandaform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data

            
            cultivo2=informacion["cultivo"]
            volumen2=informacion["volumen"]
            cosecha2=informacion["cosecha"]
            
            gran_ventas=demanda(cultivo=cultivo2,volumen=volumen2,cosecha=cosecha2)
            gran_ventas.save()
            return render(request,"MVT_app/inicio.html",{"mensaje":"su demanda se pidio correctamente"})
    else:
        formulario=demandaform()
