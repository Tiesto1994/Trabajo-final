from django.urls import path
from MVT_Ronconi_app.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('',inicio,name="inicio1"),
    path('cultivo/',Cultivo,name="cultivo"),
    path('empresas/',Empresas,name="empresa"),
    path('compras/',Compras,name="compras"),
    path('ventas/',Ventas,name="ventas"),
    path('cultivoformulario/', cultivoformulario, name="cultivoformulario"),
    path('empresaformulario/', empresaformulario, name="empresaformulario"),
    path('comprasformulario/', comprasformulario, name="comprasformulario"),
    path('ventasformulario/', ventasformulario, name="ventasformulario"),
    path('busquedacultivo/', busquedacultivo, name="busquedacultivo"),
    path('buscar/', buscar, name="buscar"),

    path('leer_empresa/', leer_empresa, name="leer_empresa"),
    path('borrar_empresa/<id>', borrar_empresa, name="borrar_empresa"),
    path('editar_empresa/<id>', editar_empresa, name="editar_empresa"),


    path('login/', login_request, name='login'),
    path('register/', register, name='register'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('editarusuario',editarusuario, name='editarusuario'),
    path('agregarAvatar',agregaravatar, name='agregarAvatar'),
    path('grupo',grupo, name='grupo'),

    path('chatconsulta/', chatconsulta1, name="chatconsulta"),
    path('leer_consulta/', leer_consulta1, name="leer_consulta"),
    
]