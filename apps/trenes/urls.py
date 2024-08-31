from django.urls import path
from .views import *

urlpatterns = [
    path('registrarTren/', registrarTren, name='tren_registrar'), #Parte logica del registro de tren
    path('', index, name='trenes_index'),
    path('register/', trenesForm, name='trenes_nuevo'),
    path('list/edit/<int:id>', editarTren, name='trenes_editar'),
    path('list/',TrenListView.as_view(), name='trenes_lista'),
    path('list/eliminarTren/<int:id>', eliminarTren), #Parte logica de eliminar tren
    
]