from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from ReservasVentasTrenes.views import pageHome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pageHome, name="base"),
    path('clientes/', include('apps.clientes.urls')),
    path('trenes/', include('apps.trenes.urls')),
    path('rutas/', include('apps.rutas.urls')),
    path('reservas/', include('apps.reservas.urls')),
    path('asientos/', include('apps.asientos.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='base'), name='logout'),
]
