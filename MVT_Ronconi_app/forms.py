from django import forms
from django.contrib.auth.forms import  UserCreationForm
from django.contrib.auth.models import User

class cultivoform(forms.Form):
    cultivo=forms.CharField(max_length=50)
    gremio=forms.CharField(max_length=50)
    cosecha=forms.CharField(max_length=50)

class empresasform(forms.Form):
    razon_social=forms.CharField(max_length=50)
    cuit=forms.IntegerField()
    gremio=forms.CharField(max_length=50)

class comprasform(forms.Form):
    razon_social=forms.CharField(max_length=50)
    cuit=forms.IntegerField()
    cultivo=forms.CharField(max_length=50)
    volumen=forms.IntegerField()
    cosecha=forms.CharField(max_length=50)
    

class ventasform(forms.Form):
    razon_social=forms.CharField(max_length=50)
    cuit=forms.IntegerField()
    cultivo=forms.CharField(max_length=50)
    volumen=forms.IntegerField()
    cosecha=forms.CharField(max_length=50)

class RegistroUsuarioForm(UserCreationForm):

    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = {k:"" for k in fields}
    
class usereditform(UserCreationForm):

    email = forms.EmailField()
    password1= forms.CharField(label="Ingrese Contraseña", widget=forms.PasswordInput)
    password2= forms.CharField(label="Repita Contraseña", widget=forms.PasswordInput)
    first_name= forms.CharField(label="modificar nombre")
    last_name= forms.CharField(label="modificar apellido")

    class Meta:
        model = User
        fields = [ "email", "password1", "password2","first_name","last_name"]
        help_texts = {k:"" for k in fields}

class AvatarForm(forms.Form):
    imagen=forms.ImageField(label="Imagen")