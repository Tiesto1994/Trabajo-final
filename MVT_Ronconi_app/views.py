from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.template import Template, loader
from MVT_Ronconi_app.forms import *
from django.urls import reverse_lazy

from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, authenticate

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required 

# Create your views here.
def Cultivo (request):
    return render(request,"MVT_app/cultivo.html")

def Empresas (request):
    return render(request,"MVT_app/empresa.html")

def Compras (request):
    return render(request,"MVT_app/compra.html")

def Ventas (request):
    return render(request,"MVT_app/venta.html")

def inicio (request):
    return render(request,"MVT_app/inicio1.html")

def grupo (request):
    return render(request,"MVT_app/grupo.html")

def inicio2 (request):
    return render(request,"MVT_app/inicio1.html")

@login_required
def cultivoformulario (request):

    if request.method=="POST":
        form=cultivoform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            cultivo1=informacion["cultivo"]
            gremio1=informacion["gremio"]
            cosecha1=informacion["cosecha"]
            gran_cultivo=cultivo(cultivo=cultivo1,gremio=gremio1,cosecha=cosecha1)
            gran_cultivo.save()
            return render(request,"MVT_app/inicio.html", {"mensaje":"cultivo creado correctamente"})
    else:
        formulario=cultivoform()


    return render(request,"MVT_app/cultivoformulario.html", {"form":formulario})
@login_required
def empresaformulario (request):

    if request.method=="POST":
        form=empresasform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            razonsocial5=informacion["razon_social"]
            cuit5=informacion["cuit"]
            gremio5=informacion["gremio"]
            gran_empresa=empresas(razon_social=razonsocial5,cuit=cuit5,gremio=gremio5)
            gran_empresa.save()
            return render(request,"MVT_app/inicio.html", {"mensaje":"Empresa creada correctamente"})
    else:
        formulario=empresasform()


    return render(request,"MVT_app/empresaformulario.html", {"form":formulario})
@login_required
def comprasformulario (request):

    if request.method=="POST":
        form=comprasform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data

            razonsocial1=informacion["razon_social"]
            cuit1=informacion["cuit"]
            cultivo1=informacion["cultivo"]
            volumen1=informacion["volumen"]
            cosecha1=informacion["cosecha"]
            
            gran_compras=compras(razon_social=razonsocial1,cuit=cuit1,cultivo=cultivo1,volumen=volumen1,cosecha=cosecha1)
            gran_compras.save()
            return render(request,"MVT_app/inicio.html", {"mensaje":"compra cargada correctamente"})
    else:
        formulario=comprasform()


    return render(request,"MVT_app/comprasformulario.html", {"form":formulario})
@login_required
def ventasformulario (request):

    if request.method=="POST":
        form=ventasform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data

            razonsocial2=informacion["razon_social"]
            cuit2=informacion["cuit"]
            cultivo2=informacion["cultivo"]
            volumen2=informacion["volumen"]
            cosecha2=informacion["cosecha"]
            
            gran_ventas=ventas(razon_social=razonsocial2,cuit=cuit2,cultivo=cultivo2,volumen=volumen2,cosecha=cosecha2)
            gran_ventas.save()
            return render(request,"MVT_app/inicio.html",{"mensaje":"venta cargada correctamente"})
    else:
        formulario=ventasform()


    return render(request,"MVT_app/ventasformulario.html", {"form":formulario})
@login_required
def busquedacultivo (request):
    return render(request,"MVT_app/busquedacultivo.html")
@login_required
def buscar (request):
    if request.GET["cultivo"]:
        cultivo94=request.GET["cultivo"]
        cultivos=cultivo.objects.filter(cultivo=cultivo94)
        return render(request,"MVT_app/resultadobusqueda.html",{"cultivo":cultivos})
    else:
        return render(request,"MVT_app/resultadobusqueda.html",{"mensaje":"fijate que no esta este cultivo"})

@login_required
def leer_empresa(request):
    empresas_lista=empresas.objects.all()
    return render(request, "MVT_app/leer_empresa.html", {"ESTO_VA":empresas_lista})
@login_required
def borrar_empresa(request, id):
    empresaeliminar=empresas.objects.get(id=id)
    empresaeliminar.delete()
    empresas_lista=empresas.objects.all()
    return render(request, "MVT_app/leer_empresa.html", {"ESTO_VA":empresas_lista})
@login_required
def editar_empresa(request, id):
    empresa=empresas.objects.get(id=id)
    if request.method=="POST":
        form=empresasform(request.POST)
        if form.is_valid():
            informacion=form.cleaned_data
            empresa.razon_social=informacion["razon_social"]
            empresa.cuit=informacion["cuit"]
            empresa.gremio=informacion["gremio"]
            
            empresa.save()
            total_empresas=empresas.objects.all()
            return render(request,"MVT_app/leer_empresa.html", {"mensaje":"Empresa creada correctamente", "ESTO_VA":total_empresas })
    else:
        formulario=empresasform(initial={"razon_social":empresa.razon_social, "cuit":empresa.cuit, "gremio":empresa.gremio  })
    return render(request, "MVT_app/editar_empresa.html", {"form":formulario, "Que_empresa":empresa})


def login_request(request):
    if request.method == "POST":
        form=AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            usu=form.cleaned_data.get("username")
            clave=form.cleaned_data.get("password")

            usuario=authenticate(username=usu, password=clave)
            if usuario is not None:    
                login(request, usuario)
                return render(request, 'MVT_app/inicio.html', {"el_mensaje":f"Bienvenido {usuario}" })
            else:
                return render(request, 'MVT_app/login.html', {"form":form, "el_mensaje":"Usuario o contraseña incorrectos"})
    else:
        form= AuthenticationForm()
        return render(request, "MVT_app/login.html", {"form":form})



def register(request):
    if request.method=="POST":
        form=RegistroUsuarioForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data.get("username")
            form.save()
           
            return render(request, 'MVT_app/inicio.html', {"el_mensaje":f"Usuario {username} ha sido creado correctamente"})
        else:
            return render(request, "MVT_app/register.html", {"form":form, "el_mensaje":"Error al crear el usuario"})
        
    else:
        form=RegistroUsuarioForm()
        return render(request, "MVT_app/register.html", {"form":form})

@login_required
def editarusuario(request):
    usuario=request.user
    if request.method=="POST":
        form:usereditform(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            usuario.email=info["email"]
            usuario.paswordd1=info["paswordd1"]
            usuario.paswordd2=info["paswordd2"]
            usuario.first_name=info["first_name"]
            usuario.last_name=info["last_name"]
            usuario.save()
            return render(request, "MVT_app/inicio.html", {"mensaje":"usuario editado correctamente"})
    else:
        form=usereditform(instance=usuario)
        return render(request,"MVT_app/editarusuario.html",{"form":form, "nombreusuario":usuario.username})

@login_required
def agregaravatar(request):
    if request.method=="POST":
        form=AvatarForm(request.POST, request.FILES)
        if form.is_valid():
            avatarViejo=Avatar.objects.filter(user=request.user)
            if len(avatarViejo)!=0:
                avatarViejo[0].delete()
            avatar=Avatar(user=request.user, imagen=request.FILES["imagen"])
            avatar.save()
            return render(request, "MVT_app/inicio.html", {"mensaje":"El Avatar se agrego correctamente"})
        else:
            return render(request, "MVT_app/agregaravatar.html", {"formulario": form, "usuario": request.user})
    else:
        form=AvatarForm()
        return render(request , "MVT_app/agregaravatar.html", {"formulario": form, "usuario": request.user})
