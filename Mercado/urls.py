from django.urls import path
from Mercado.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('oferta/',oferta,name="oferta"),
    path('demanda/',demanda,name="demanda"),
    
]