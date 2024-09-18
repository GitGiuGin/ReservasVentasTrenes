from django.shortcuts import render
from apps.trenes.models import Tren
from apps.rutas.models import Ruta
from apps.reservas.models import Reserva
from apps.asientos.models import Asiento
from datetime import datetime

# Create your views here.
def obtenerFechaActual(request):
    fecha_actual = datetime.now().strftime("%d/%m/%Y")
    return fecha_actual

def liberarAsiento(asiento_id):
    try:
        asiento = Asiento.objects.get(id=asiento_id)
        asiento.estado = False
        asiento.reserva = None
        asiento.save()
        return True
    except Asiento.DoesNotExist:
        return False

def obtenerEstado(asiento_id):
    try:
        asiento = Asiento.objects.get(id=asiento_id)
        if asiento.estado == 1:
            return ""
        else:
            return "checked"
    except Asiento.DoesNotExist:
        return False

def formSelectAsiento(request, id):
    fecha_actual = obtenerFechaActual(request)
    ruta = Ruta.objects.get(id=id)
    asientos = Asiento.objects.filter(ruta_id = ruta.id)
    asientos_disponibles = verificarDisponibilidad(ruta_id = id)
    
    asientos_con_estado = []
    for asiento in asientos:
        estado = obtenerEstado(asiento.id)
        asientos_con_estado.append({
            'id': asiento.id,
            'numero_asiento': asiento.numero_asiento,
            'asiento': asiento,
            'estado': estado
        })
    
    data = {
        "ruta": ruta,
        "fecha_actual": fecha_actual,
        "asientos": asientos_con_estado,
        'asientos_disponibles': asientos_disponibles
    }
    
    return render(request, 'asientos/seleccion_asiento.html', data)

def verificarDisponibilidad(ruta_id):
    asientos_disponibles = Asiento.objects.filter(ruta_id=ruta_id, estado=1).count()
    return asientos_disponibles

def obtenerTrenes(request):
    trenes_activos = Tren.objects.filter(estado=True)
    
