from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='trenes_index'),
    path('register/', trenesForm, name='trenes_nuevo'),
    path('registrarTren/', registrarTren, name='tren_registrar'),
    path('list/edicionTren/<int:id>', trenEdicion, name='tren_edicion'),
    path('list/',TrenListView.as_view(), name='trenes_lista'),
    path('list/editarTren', editarTren, name="tren_editar"),
]