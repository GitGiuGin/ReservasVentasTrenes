from django.urls import path
from .views import index, clientesNew, clientesEditar, clientesList

urlpatterns = [
    path('', index, name='clientes_index'),
    path('register/', clientesNew, name='clientes_nuevo'),
    path('edit/', clientesEditar, name='clientes_editar'),
    path('list/', clientesList, name='clientes_lista'),
]