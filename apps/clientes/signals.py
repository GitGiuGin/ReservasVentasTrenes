from django.db.models.signals import post_migrate
from django.dispatch import receiver
from .models import Cliente

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