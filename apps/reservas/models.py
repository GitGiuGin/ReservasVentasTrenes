from django.db import models
from apps.clientes.models import Cliente
from apps.rutas.models import Ruta

# Create your models here.
class Reserva (models.Model):
    fecha_reserva = models.DateField(verbose_name='Fecha de Reserva', null=True, blank=True)
    estado = models.BooleanField(default=False)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    ruta = models.ForeignKey(Ruta, on_delete=models.CASCADE, null=True, blank=True, related_name='reservas')
    
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        db_table = 'reserva'
        ordering = ['fecha_reserva', 'cliente']
        
class ReservaAsiento(models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='reservas_asientos')
    asiento = models.ForeignKey("asientos.Asiento", on_delete=models.CASCADE, related_name='reservas_asientos')
    estado = models.BooleanField(default=True, verbose_name="Estado del Asiento en la Reserva")

    class Meta:
        verbose_name = "Reserva Asiento"
        verbose_name_plural = "Reservas Asientos"
        db_table = 'reserva_asiento'
        unique_together = ('reserva', 'asiento')  # Garantiza que no haya duplicados de la misma combinación reserva-asiento
        