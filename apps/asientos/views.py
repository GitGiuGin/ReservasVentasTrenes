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
        return "Reservado" if asiento.estado else "Disponible"
    except Asiento.DoesNotExist:
        return "Asiento no encontrado"

def formSelectAsiento(request, id):
    fecha_actual = obtenerFechaActual(request)
    ruta = Ruta.objects.get(id=id)
    asientos = Asiento.objects.values_list('numero_asiento', flat=True)
    #eserva = Reserva.objects.all()
    
    data = {
        "ruta": ruta,
        "fecha_actual": fecha_actual,
        "asientos": list(asientos),
        #"reserva": reserva,
    }
    
    return render(request, 'asientos/seleccion_asiento.html', data)

def verificarDisponibilidad(ruta_id):
    asientos_disponibles = Asiento.objects.filter(ruta_id=ruta_id, estado=False).count()
    return asientos_disponibles > 0

def obtenerTrenes(request):
    trenes_activos = Tren.objects.filter(estado=True)
    
