from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from .models import Proveedor, Marca, Vehiculo, Repuesto
# from .serializers import ProveedorSerializer, MarcaSerializer, VehiculoSerializer, RepuestoSerializer

# class ProveedorViewSet(viewsets.ModelViewSet):
#     queryset = Proveedor.objects.all()
#     serializer_class = ProveedorSerializer

# class MarcaViewSet(viewsets.ModelViewSet):
#     queryset = Marca.objects.all()
#     serializer_class = MarcaSerializer

# class VehiculoViewSet(viewsets.ModelViewSet):
#     queryset = Vehiculo.objects.all()
#     serializer_class = VehiculoSerializer

# class RepuestoViewSet(viewsets.ModelViewSet):
#     queryset = Repuesto.objects.all()
#     serializer_class = RepuestoSerializer