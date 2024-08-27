from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='trenes_index'),
    path('register/', trenesNew, name='trenes_nuevo'),
    path('edit/', trenesEditar, name='trenes_editar'),
    path('list/',TrenListView.as_view(), name='trenes_lista'),
    path('list/eliminarTren/<int:id>', eliminarTren), #Parte logica de eliminar tren
    path('registrarTren/', registrarTren, name='tren_registrar'), #Parte logica del registro de tren
    path('editarTren/', registrarTren, name='tren_editar'),
]