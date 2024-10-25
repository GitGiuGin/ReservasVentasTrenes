from django.db import models
from django.conf import settings
from apps.trenes.models import Tren
from datetime import datetime

# Create your models here.
class Ruta (models.Model):
    ORIGEN_CHOICES = [('estacion1', 'Estación 1'), ('estacion2', 'Estación 2')]  # Ejemplo de opciones
    DESTINO_CHOICES = [('estacionA', 'Estación A'), ('estacionB', 'Estación B')]  # Ejemplo de opciones
    
    origen = models.CharField(max_length=50, verbose_name="Estación de origen", choices=ORIGEN_CHOICES)
    destino = models.CharField(max_length=50, verbose_name="Estación de destino", choices=DESTINO_CHOICES)
    duracion = models.TimeField()
    dia_salida = models.CharField(max_length=50, verbose_name="Dia Salida", null=True, blank=True)
    horario_salida = models.TimeField(verbose_name="Horario de Salida", null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tren = models.ForeignKey(Tren, null=True, blank=True, on_delete=models.CASCADE)
    
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Ruta")
        verbose_name_plural = ("Rutas")
        db_table = 'ruta'

    def ruta_completa(self):
        return "{} - {}".format(self.origen, self.destino)
    
    def precio_bs(self):
        return f"{self.precio} Bs"

    def duracion_formateada(self):
        """Retorna la duración en formato HH:MM."""
        horas = self.duracion.hour
        minutos = self.duracion.minute
        return f"{horas:02}:{minutos:02} hrs"

    def horario_salida_formateado(self):
        if self.horario_salida:
            hour = self.horario_salida.hour
            minute = self.horario_salida.minute
            period = "a.m." if hour < 12 else "p.m."
            return f"{hour:02}:{minute:02} {period}"
        return None