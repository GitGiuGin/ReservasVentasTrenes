from django.urls import path
from .views import *

urlpatterns = [
    path('clientes/PDF/', reporte_clientes_pdf, name='reporte_clientes_pdf'),
    path('ventas/', reporte_ventas, name='reporte_ventas'),
    path('viajes-realizados', viajes_realizados, name='viajes_realizados'),
    path('ruta<int:ruta_id>', clientes_por_ruta, name='clientes_por_ruta'),
    path('clientes_por_ruta_pdf/<int:ruta_id>/', clientes_por_ruta_pdf, name='clientes_por_ruta_pdf'),
]