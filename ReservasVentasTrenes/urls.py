from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from ReservasVentasTrenes.views import pageHome

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', pageHome, name="base"),
    path('clientes/', include('apps.clientes.urls')),
    path('trenes/', include('apps.trenes.urls')),
    path('rutas/', include('apps.rutas.urls')),
    path('reservas/', include('apps.reservas.urls')),
    path('asientos/', include('apps.asientos.urls')),
    path('asientos/', include('apps.pagos.urls')),
    path('reportes/', include('apps.reportes.urls')),
    path('logout/', auth_views.LogoutView.as_view(next_page='base'), name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)