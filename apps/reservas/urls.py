from django.urls import path
from .views import *

urlpatterns = [
    path('register/', nuevaReserva, name='reserva_nuevo'),
    path('list/', ReservaListView.as_view(), name='reserva_lista'),
    path('registrarReserva/', registrarReserva, name='reserva_registrar'),
    path('confirmarReserva/', confirmarFormReserva, name='confirmar_reserva'),
    path('edit/<int:reserva_id>', confEditarReserva, name='reserva_editar'),
    path('reservaEditada/<int:reserva_id>', editarReserva, name='reserva_editada'),
    path('delete/<int:reserva_id>', cancelar_reserva, name='cancelar_reserva'),
]