from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Barrio(models.Model):
    barrio = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.barrio}'

class Establecimiento(models.Model):
    establecimiento = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.establecimiento}'
class Cliente(models.Model):
    CC = models.CharField(max_length=255)
    nombre = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    telefono = models.CharField(max_length=255)
    residencia = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} '


class Cuenta(models.Model):
    id_Cliente = models.ForeignKey(Cliente, on_delete=models.SET_NULL, null=True,limit_choices_to={'estado': True})
    establecimiento = models.ForeignKey(Establecimiento, on_delete=models.SET_NULL, null=True,limit_choices_to={'estado': True})
    barrio = models.ForeignKey(Barrio, on_delete=models.SET_NULL, null=True,limit_choices_to={'estado': True})
    direccion = models.CharField(max_length=255, null=True)
    saldo = models.IntegerField()
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} {self.id_Cliente} {self.establecimiento} {self.barrio} {self.direccion} {self.saldo}'


class Recaudos(models.Model):
    id_cuenta = models.ForeignKey(Cuenta, on_delete=models.SET_NULL, null=True,limit_choices_to={'estado': True})
    fecha_pago = models.DateTimeField(auto_now_add=True)
    monto = models.IntegerField(max_length=255)
    estado = models.BooleanField(default=True)

class Pagos(models.Model):
    fecha_pago = models.DateTimeField(auto_now_add=True)
    descripcion = models.CharField(max_length=255)
    monto = models.IntegerField(max_length=255)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id} {self.fecha_pago} {self.descripcion} {self.monto}'