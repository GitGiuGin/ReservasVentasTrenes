from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='clientes_index'),
    path('register/', clientesForm, name='clientes_nuevo'),
    path('edit/', clientesEditar, name='clientes_editar'),
    path('list/', ClienteListView.as_view(), name='clientes_lista'),
    path('list/eliminarCliente/<int:id>', eliminarCliente), #Parte logica de eliminar cliente
    path('registrarCliente/', registrarCliente, name='cliente_registrar'), #Parte logica del registro de cliente
]