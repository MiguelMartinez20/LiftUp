from .models import Tecnico, Cliente, FormaTrabajo
from rest_framework import serializers

class TecnicoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tecnico
        fields = ('nombre','email', 'password')

class ClienteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Cliente
        fields = ('nombre','direccion', 'ciudad', 'comuna' , 'telefono', 'email')


class FormaTrabajoSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = FormaTrabajo
        fields = ('cliente','fecha', 'horaini', 'horater', 'numasc', 'modeloasc', 'fallas', 'reparacion', 'piezas', 'tecnico')
