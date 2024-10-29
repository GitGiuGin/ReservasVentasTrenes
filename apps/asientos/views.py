from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from apps.trenes.models import Tren
from apps.rutas.models import Ruta
from apps.reservas.models import Reserva, ReservaAsiento
from apps.asientos.models import Asiento
from datetime import datetime


# Create your views here.
def obtenerFechaActual(request):
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    return fecha_actual

def liberarAsiento(asiento_id):
    try:
        reserva_asiento  = ReservaAsiento.objects.get(id=asiento_id)
        reserva_asiento.estado = False
        reserva_asiento.reserva = None
        reserva_asiento.save()
        return True
    except Asiento.DoesNotExist:
        return False

def obtenerEstado(asiento_id, ruta_id):
    try:
        # Busca el estado en la tabla intermedia ReservaAsiento
        reserva_asiento = ReservaAsiento.objects.get(asiento_id=asiento_id, reserva__ruta_id=ruta_id)
        return "checked" if not reserva_asiento.estado else ""
    except ReservaAsiento.DoesNotExist:
        # Si no existe una reserva, significa que está disponible
        return ""

@login_required(login_url='login')
def formSelectAsiento(request, id):
    usuario = request.user
    fecha_actual = obtenerFechaActual(request)
    ruta = Ruta.objects.get(id=id)
    tren = ruta.tren
    asientos_disponibles = verificarDisponibilidad(ruta_id = ruta.id)
    total_asientos_disponibles = asientos_disponibles.count()
    asientos = Asiento.objects.all()
    for asiento in asientos:
        asiento.estado_check = obtenerEstado(asiento.id, ruta.id)
        
    data = {
        "ruta": ruta,
        "fecha_actual": fecha_actual,
        "asientos": asientos,
        "usuario": usuario,
        "tren": tren,
        "asientos_disponibles" : total_asientos_disponibles
    }
    
    return render(request, 'asientos/seleccion_asiento.html', data)

def verificarDisponibilidad(ruta_id):
    asientos_disponibles = Asiento.objects.exclude(
        reservas_asientos__reserva__ruta_id=ruta_id, 
        reservas_asientos__estado=False
    )
    if asientos_disponibles == 0:
        return "Sin asientos disponibles"
    
    return asientos_disponibles

def obtenerTrenes(request):
    trenes_activos = Tren.objects.filter(estado=True)
    
