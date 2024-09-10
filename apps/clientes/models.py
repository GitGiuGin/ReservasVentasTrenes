from django.db import models

# Create your models here.
class Cliente (models.Model):
    nombres = models.CharField(max_length=50, verbose_name="Nombres")
    apellido_paterno = models.CharField(max_length=50, verbose_name="Apellido_paterno")
    apellido_materno = models.CharField(max_length=50, verbose_name="Apellido_materno")
    correo = models.CharField(max_length=128, verbose_name="Correo")
    telefono = models.CharField(max_length=15, verbose_name="Telefono")
    direccion = models.CharField(max_length=255, verbose_name="Direccion")
    contraseña = models.CharField(max_length=128, default='defaultpassword', verbose_name="Contraseña")
    estado = models.BooleanField(default=True)
    
    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"
        db_table = 'cliente'
        ordering = ['apellido_paterno', '-apellido_materno', 'nombres']

    def nombre_completo(self):
        return "{} {}, {}".format(self.apellido_paterno, self.apellido_materno, self.nombres)
    
    def __str__(self):
        return self.nombre_completo()
    
    @property
    def estado_display(self):
        return "Activo" if self.estado else "Inactivo"
    

