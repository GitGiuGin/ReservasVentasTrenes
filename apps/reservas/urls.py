from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
    path('register/', reservaForm, name='reserva_nuevo'),
    path('edit/', reservaEditar, name='reserva_editar'),
    path('list/', ReservaListView.as_view(), name='reserva_lista'),
    path('list/eliminarReserva/<int:id>', eliminarReserva), #Parte logica de eliminar cliente
    path('registrarReserva/', registrarReserva, name='reserva_registrar'),
    path('confirmarReserva/', confirmarFormReserva, name='confirmar_reserva'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)