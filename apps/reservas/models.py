from django.db import models
from apps.clientes.models import Cliente
from apps.trenes.models import Tren
from django.core.exceptions import ValidationError

# Create your models here.
def validar_pdf(value):
    if not value.name.endswith('.pdf'):
        raise ValidationError('Solo se permiten archivos PDF.')
    
class Reserva (models.Model):
    CHOISES_RESERVA = [] # ["Disponible", "Confirmado", "Modificado", "Cancelado", "Finalizado"]
    fecha_reserva = models.DateField(verbose_name='Fecha de Reserva')
    estado = models.BooleanField(default=False, choices=CHOISES_RESERVA)
    numero_comprobante = models.CharField(max_length=20, verbose_name="Numero de comprobante")
    documento_comprobante = models.FileField(upload_to='comprobantes/', verbose_name="Documento Comprobante", validators=[validar_pdf])
    cliente = models.ForeignKey(Cliente, null=True, blank=True, on_delete=models.CASCADE)
    tren = models.ForeignKey(Tren, null=True, blank=True, on_delete=models.CASCADE)
    
    class Meta:
        verbose_name = "Reserva"
        verbose_name_plural = "Reservas"
        db_table = 'reserva'
        ordering = ['fecha_reserva', 'cliente']
        