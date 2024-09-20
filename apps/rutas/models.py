from django.db import models
from apps.trenes.models import Tren
from datetime import datetime

# Create your models here.
class Ruta (models.Model):
    ORIGEN_CHOICES = [('estacion1', 'Estación 1'), ('estacion2', 'Estación 2')]  # Ejemplo de opciones
    DESTINO_CHOICES = [('estacionA', 'Estación A'), ('estacionB', 'Estación B')]  # Ejemplo de opciones
    
    origen = models.CharField(max_length=50, verbose_name="Estación de origen", choices=ORIGEN_CHOICES)
    destino = models.CharField(max_length=50, verbose_name="Estación de destino", choices=DESTINO_CHOICES)
    duracion = models.SmallIntegerField()
    dia_salida = models.CharField(max_length=50, verbose_name="Dia Salida", null=True, blank=True)
    horario_salida = models.TimeField(verbose_name="Horario de Salida", null=True, blank=True)
    dia_retorno = models.CharField(max_length=50, verbose_name="Dia Retorno", null=True, blank=True)
    horario_retorno = models.TimeField(verbose_name="Horario de Salida", null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tren = models.ForeignKey(Tren, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Ruta")
        verbose_name_plural = ("Rutas")
        db_table = 'ruta'

    def ruta_completa(self):
        return "{} - {}".format(self.origen, self.destino)
    
    def duracion_formateada(self):
        horas = self.duracion // 60
        minutos = self.duracion % 60
        return f"{horas}:{minutos:02d} hrs"
    
    def precio_bs(self):
        return f"{self.precio} Bs"
    
    def formato_horario_retorno(self):
        if self.horario_retorno:
            return self.horario_retorno.strftime('%H:%M')  # Formato HH:MM
        return None