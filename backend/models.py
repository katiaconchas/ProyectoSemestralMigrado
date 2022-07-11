
# Create your models here.
from django.db import models
class Usuario(models.Model):
    email = models.EmailField(primary_key=True)
    nombre = models.CharField(max_length=100)
    password= models.CharField(max_length=15)
    

    def __str__(self):
        return self.nombre

class Usuario_signup(models.Model):
    email = models.EmailField(primary_key=True)
    password = models.CharField(max_length=15)
    pnombre = models.CharField(max_length=50)
    appaterno = models.CharField(max_length=50)