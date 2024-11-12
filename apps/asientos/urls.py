from django.urls import path
from .views import *

urlpatterns = [
    path('reserve/<int:id>', formSelectAsiento, name='seleccion_asiento'),
    path('edit/<int:reserva_id>/ruta<int:ruta_id>/', formEditAsiento, name='editar_asiento'),
]