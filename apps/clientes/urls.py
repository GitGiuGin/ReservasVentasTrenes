from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='clientes_index'),
    path('register/', clientesForm, name='clientes_nuevo'),
    path('registrarCliente/', registrarCliente, name='cliente_registrar'), #Parte logica del registro de cliente
    path('list/edicionCliente/<int:id>', clientesEdicion, name='clientes_edicion'),
    path('list/', ClienteListView.as_view(), name='clientes_lista'),
    path('list/editarCliente', editarCliente, name="clientes_editar"),
]