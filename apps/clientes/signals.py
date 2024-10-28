from django.db.models.signals import post_migrate
from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Cliente
from apps.asientos.models import Asiento

@receiver(post_migrate)
def create_superuser(sender, **kwargs):
    if sender.name == 'apps.clientes':  # Verifica que este sea el nombre correcto de tu aplicación
        if not Cliente.objects.filter(correo='adminutb@gmail.com').exists():  # Cambia el correo si es necesario
            Cliente.objects.create_superuser(
                correo='adminutb@gmail.com',
                nombres='Jean Marco',
                apellido_paterno='Gutierrez',
                apellido_materno='Espejo',
                password='adminutb'  # Cambia la contraseña según tus necesidades
            )
            
@receiver(post_save, sender=Asiento)
def eliminar_relacion_reserva(sender, instance, **kwargs):
    # Verifica si el estado cambió a True
    if instance.estado:
        # Elimina la relación del asiento con la reserva (si existe)
        instance.reserva = None
        instance.save()