# Python native imports
from django.shortcuts import render

# External imports
from rest_framework import viewsets
from django.utils import timezone as tz

# Local imports
from repuestos.models import *
from repuestos.serializers import *

class ProveedorViewSet(viewsets.ModelViewSet):
     queryset = Proveedor.objects.all()
     serializer_class = ProveedorSerializer

class MarcaViewSet(viewsets.ModelViewSet):
     queryset = Marca.objects.all()
     serializer_class = MarcaSerializer

class VehiculoViewSet(viewsets.ModelViewSet):
     queryset = Vehiculo.objects.all()
     serializer_class = VehiculoSerializer

class RepuestoViewSet(viewsets.ModelViewSet):
     queryset = Repuesto.objects.all()
     serializer_class = RepuestoSerializer