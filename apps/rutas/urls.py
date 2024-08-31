from django.urls import path
from .views import *

urlpatterns = [
    path('registrarRuta/', registrarRuta, name='ruta_registrar'),
    path('', index, name='ruta_index'),
    path('register/', rutaForm, name='ruta_nuevo'),
    path('edit/', editarRuta, name='ruta_editar'),
    path('list/',RutaListView.as_view(), name='ruta_lista'),
    path('list/eliminarRuta/<int:id>', eliminarRuta),
    
]