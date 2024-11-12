from django.contrib.auth import views as auth_views
from django.urls import path
from .views import *

urlpatterns = [
    path('register/', clientesForm, name='clientes_nuevo'),
    path('registrarCliente/', registrarCliente, name='cliente_registrar'), #Parte logica del registro de cliente
    path('list/edicionCliente/<int:id>/<str:next>', clientesEdicion, name='clientes_edicion'),
    path('registrarDesdeLogin/', registro_cliente_desde_login, name='cliente_registrar_login'),
    path('list/', ClienteListView.as_view(), name='clientes_lista'),
    path('list/editarCliente', editarCliente, name="clientes_editar"),
    path('login/', custom_login_view, name='login'),
    path('account/', perfil_usuario, name='mi_cuenta'),
    path('reservas/', reservas_usuario, name='mis_reservas'),
    path('detalle_reserva/<int:reserva_id>/', detalle_reserva, name='detalle_reserva'),
    path('detalle_reserva/<int:reserva_id>/pdf/', detalle_reserva, {'generar_pdf': True}, name='generar_ticket'),
    path('enviar_ticket/<int:reserva_id>/', enviar_ticket_por_email, name='enviar_ticket'),
]