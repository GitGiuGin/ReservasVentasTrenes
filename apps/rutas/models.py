from django.db import models
from django.conf import settings
from apps.trenes.models import Tren
from datetime import datetime

# Create your models here.
class Ruta (models.Model):
    origen = models.CharField(max_length=50, verbose_name="Estación de origen")
    destino = models.CharField(max_length=50, verbose_name="Estación de destino")
    duracion = models.TimeField()
    fecha_salida = models.DateField(verbose_name='Dia salida', null=True, blank=True)
    hora_salida = models.TimeField(verbose_name="Horario de Salida", null=True, blank=True)
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
        horas = self.duracion.hour
        minutos = self.duracion.minute
        return f"{horas:02}:{minutos:02} hrs"

    def horario_salida_formateado(self):
        if self.hora_salida:
            hour = self.hora_salida.hour
            minute = self.hora_salida.minute
            period = "a.m." if hour < 12 else "p.m."
            return f"{hour:02}:{minute:02} {period}"
        return None
    
    @property
    def fecha_salida_formateada(self):
        if self.fecha_salida:
            return self.fecha_salida.strftime("%d/%m/%Y")  # Formato DD/MM/AAAA
        return "No definida"