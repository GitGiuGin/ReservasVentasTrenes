from django.urls import path
from .views import *

urlpatterns = [
    path('seleccionaAsiento', reservasAsiento, name='seleccion_asiento'),
]