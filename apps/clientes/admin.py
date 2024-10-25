from django.contrib import admin
from .models import Cliente

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('nombres', 'apellido_paterno', 'apellido_materno', 'correo', 'telefono', 'direccion', 'tipo_usuario', 'is_active')
    search_fields = ['nombres', 'apellido_paterno', 'apellido_materno', 'correo']
    list_filter = ('tipo_usuario', 'is_active')  # Filtrar por tipo de usuario y estado (activo/inactivo)

# Registrar el modelo Cliente en el admin
admin.site.register(Cliente, ClienteAdmin)