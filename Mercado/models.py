from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class oferta (models.Model):
   
    cultivo=models.CharField(max_length=50)
    volumen=models.IntegerField()
    cosecha=models.CharField(max_length=50)
    
    def __str__(self):
        return  self.cultivo +""+ str(self.volumen) +""+ self.cosecha 

class demanda (models.Model):
    
    cultivo=models.CharField(max_length=50)
    volumen=models.IntegerField()
    cosecha=models.CharField(max_length=50)
    
    def __str__(self):
        return  self.cultivo +""+ str(self.volumen) +""+ self.cosecha 