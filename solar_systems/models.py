from django.db import models

# Create your models here.
class PanelSolar(models.Model):
    nombre=models.CharField(max_length=100)
    potencia = models.DecimalField(max_digits=6, decimal_places=2)  # Ejemplo: 300.00 W
    eficiencia = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo: 18.50 %
    voltaje_operacion = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo: 40.00 V
    corriente_operacion = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo: 8.00 A
    fabricante = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)  # Ejemplo: 200.00 USD

    def __str__(self):
        return self.nombre
    
class ControladorDeCarga(models.Model):
    nombre = models.CharField(max_length=100)
    corriente_nominal = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo: 30.00 A
    voltaje_entrada_max = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo: 100.00 V
    tipo = models.CharField(max_length=50)  # Ejemplo: MPPT, PWM
    eficiencia = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo: 98.00 %
    fabricante = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)  # Ejemplo: 150.00 USD

    def __str__(self):
        return self.nombre
    
class Bateria(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.DecimalField(max_digits=6, decimal_places=2)  # Ejemplo: 10.00 kWh
    voltaje = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo: 48.00 V
    tipo = models.CharField(max_length=50)  # Ejemplo: Litio, AGM, Gel
    profundidad_descarga = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo: 80.00 %
    fabricante = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)  # Ejemplo: 500.00 USD

    def __str__(self):
        return self.nombre
class Inversor(models.Model):
    nombre = models.CharField(max_length=100)
    potencia_maxima = models.DecimalField(max_digits=6, decimal_places=2)  # Ejemplo: 5000.00 W
    eficiencia = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo: 95.00 %
    voltaje_entrada_min = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo: 100.00 V
    voltaje_entrada_max = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo: 600.00 V
    salida_ac = models.DecimalField(max_digits=5, decimal_places=2)  # Ejemplo: 230.00 V
    fabricante = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2)  # Ejemplo: 1000.00 USD

    def __str__(self):
        return self.nombre

class SistemaFotovoltaico(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=255)
    tipo_sistema = models.CharField(max_length=50)  # Ejemplo: On-Grid, Off-Grid
    consumo_diario = models.DecimalField(max_digits=6, decimal_places=2)  # Ejemplo: 30.00 kWh
    paneles = models.ManyToManyField(PanelSolar)
    inversores = models.ManyToManyField(Inversor)
    baterias = models.ManyToManyField(Bateria, blank=True)  # Solo para sistemas Off-Grid
    controladores = models.ManyToManyField(ControladorDeCarga, blank=True)  # Solo si se usan controladores de carga
    costo_total = models.DecimalField(max_digits=12, decimal_places=2)  # Ejemplo: 15000.00 USD

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contraseña = models.CharField(max_length=128)  # Se manejará en forma segura

    def __str__(self):
        return self.nombre