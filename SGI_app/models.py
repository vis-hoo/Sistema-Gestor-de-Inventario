from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    email = models.EmailField()
    cargo = models.CharField(max_length=50)
    estado = models.BooleanField()

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    codigoBarras = models.CharField(max_length=100)
    descripcion = models.TextField()
    precioCompra = models.FloatField()
    precioVenta = models.FloatField()
    stockActual = models.FloatField()
    stockMinimo = models.FloatField()
    estado = models.BooleanField()