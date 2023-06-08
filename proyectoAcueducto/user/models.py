from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Tipo(models.Model):
    tipo_usuario = models.CharField(max_length=255)
    estado = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.id}'

class User(AbstractUser):
    tipo = models.ForeignKey(Tipo, on_delete=models.SET_NULL, null=True,limit_choices_to={'estado': True})