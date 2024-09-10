from django.db import models
from apps.trenes.models import Tren

# Create your models here.
class Ruta (models.Model):
    origen = models.CharField(max_length=50, verbose_name="Estacion de origen")
    destino = models.CharField(max_length=50, verbose_name="Estacion de destino")
    duracion = models.SmallIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    tren = models.ForeignKey(Tren, null=True, blank=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = ("Ruta")
        verbose_name_plural = ("Rutas")
        db_table = 'ruta'

    def ruta_completa(self):
        return "{} - {}".format(self.orgien, self.destino)