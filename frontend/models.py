from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name='ID Producto')
    nombre= models.CharField(max_length=30, verbose_name='Nombre')
    precio = models.IntegerField(verbose_name='Precio')
    stock = models.IntegerField(verbose_name='Stock')

    def _str_(self):
        return self.nombre