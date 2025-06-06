from django.db import models

class Proveedor(models.Model):
    nombre = models.CharField(max_length=100)
    contacto = models.CharField(max_length=100)
    email = models.EmailField()
    ubicacion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Marca(models.Model):
    nombre = models.CharField(max_length=100)
    pais_origen = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Vehiculo(models.Model):
    modelo = models.CharField(max_length=100)
    año = models.PositiveIntegerField()
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE, related_name="vehiculos")

    def __str__(self):
        return f"{self.modelo} ({self.año})"

class Repuesto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    moneda = models.CharField(max_length=3, choices=[("USD", "Dólares"), ("BOB", "Bolivianos")], default="BOB")
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name="repuestos")
    vehiculos = models.ManyToManyField(Vehiculo, related_name="repuestos")

    def __str__(self):
        return self.nombre