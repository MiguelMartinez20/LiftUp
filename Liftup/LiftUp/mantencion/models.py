from django.db import models
from django.utils import timezone


class Tecnico(models.Model):
    nombre = models.CharField(max_length = 50)
    email = models.CharField(max_length = 255)
    password = models.CharField(max_length=30)

class Cliente(models.Model):

    nombre = models.CharField(max_length = 60)
    direccion = models.CharField(max_length = 50)
    ciudad = models.CharField(max_length = 30)
    comuna = models.CharField(max_length = 30)
    telefono = models.CharField(max_length = 12)
    email = models.CharField(max_length = 100)

class FormaTrabajo(models.Model):

    cliente = models.CharField(max_length = 60)
    fecha = models.DateField(blank=True, null=True)
    horaini = models.DateTimeField(blank=True, null=True)
    horater = models.DateTimeField(blank=True, null=True)
    numasc = models.IntegerField()
    modeloasc = models.CharField(max_length=30)
    fallas = models.CharField(max_length=200)
    reparacion = models.CharField(max_length=200)
    piezas = models.CharField(max_length=200)
    tecnico = models.CharField(max_length=60)
    
    def fechaini_publicada(self):
        self.horaini = timezone.now()
        self.save()

    def fechaTER_publicada(self):
        self.horaTER = timezone.now()
        self.save()
