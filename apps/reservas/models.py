from django.db import models
from apps.clientes.models import Cliente
from apps.trenes.models import Tren


# Create your models here.
class Reserva (models.Model):
    fecha_reserva = models.DateField(verbose_name='Fecha de Reserva')
    estado = models.BooleanField(default=False)
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    tren = models.ForeignKey(Tren, null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        db_table = 'reserva'
        ordering = ['fecha_reserva', 'cliente']
        