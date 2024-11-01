from django.urls import path
from .views import *

urlpatterns = [
    path('register/', nuevaReserva, name='reserva_nuevo'),
    path('list/', ReservaListView.as_view(), name='reserva_lista'),
    path('list/eliminarReserva/<int:id>', eliminarReserva), #Parte logica de eliminar cliente
    path('registrarReserva/', registrarReserva, name='reserva_registrar'),
    path('confirmarReserva/', confirmarFormReserva, name='confirmar_reserva'),
    path('edit/<int:reserva_id>', confEditarReserva, name='reserva_editar'),
    path('reservaEditada/<int:reserva_id>', editarReserva, name='reserva_editada'),
]