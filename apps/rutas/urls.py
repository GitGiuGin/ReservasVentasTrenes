from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='ruta_index'),
    path('register/', rutaForm, name='ruta_nuevo'),
    path('registrarRuta/', registrarRuta, name='ruta_registrar'),
    path('list/edicionRuta/<int:id>', rutaEdicion, name='ruta_edicion'),
    path('list/',rutaLista, name='ruta_lista'),
    path('list/eliminarRuta/<int:id>', eliminarRuta),
    path('list/editarRuta', editarRuta, name="ruta_editar"),
    path('planificaTuViaje/', rutas_disponibles, name="ruta_disponible"),  
]