from rest_framework import generics
from .models import Tecnico, Cliente, FormaTrabajo
from .serializers import TecnicoSerializer, ClienteSerializer, FormaTrabajoSerializer
from django.shortcuts import render, get_object_or_404


class TecnicoList(generics.ListCreateAPIView):
    queryset = Tecnico.objects.all()
    serializer_class = TecnicoSerializer

    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj

class ClienteList(generics.ListCreateAPIView):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer

    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj       

class FormaTrabajoList(generics.ListCreateAPIView):
    queryset = FormaTrabajo.objects.all()
    serializer_class = FormaTrabajoSerializer

    def get_object(self):
        queryset = self.queryset()
        obj = get_object_or_404(
            queryset,
            pk = self.kwargs['pk'],
        )
        return obj     