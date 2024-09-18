from django.db import models
from apps.reservas.models import Reserva
from apps.rutas.models import Ruta

# Create your models here.
class Asiento (models.Model):
    numero_asiento = models.CharField(max_length=20, verbose_name="Numero Asiento")
    estado = models.BooleanField(default=False)
    reserva = models.ForeignKey(Reserva, null=True, blank=True, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Asiento"
        verbose_name_plural = "Asientos"
        db_table = 'asiento'
        ordering = ['numero_asiento']
        
    def __str__(self):
        return f'{self.numero_asiento}'