from django.db import models

# Create your models here.
class Tren (models.Model):
    nombre = models.CharField(max_length=50, verbose_name="Nombre")
    capacidad = models.SmallIntegerField()
    estado = models.BooleanField(default=True)

    class Meta:
        verbose_name = ("Tren")
        verbose_name_plural = ("Trenes")
        db_table = 'tren'
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


