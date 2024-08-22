from django.urls import path
from .views import index

urlpatterns = [
    path('', index, name='clientes_index'),  # Ruta principal para 'clientes/'
    # Puedes agregar más rutas aquí
]