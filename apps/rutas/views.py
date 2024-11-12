from django.shortcuts import render, redirect
from django.db import models
from django.db import transaction
from django.db.models import Q
from django.views.generic import ListView
from django.contrib import messages
from django.utils import timezone
from .models import Ruta
from apps.trenes.models import Tren
from apps.asientos.models import Asiento
from apps.reservas.models import Reserva
from datetime import datetime
from django import forms
from apps.asientos.views import verificarDisponibilidad

# Create your views here.

def index (request):
    pass

def rutaForm(request):
    trenes_activos = Tren.objects.filter(estado=True)
    return render(request, 'rutas/ruta_form.html', {'trenes': trenes_activos})

def registrarRuta(request):
    if request.method == 'POST':
        origen = request.POST.get('txtOrigen').title()
        destino = request.POST.get('txtDestino').title()
        duracion = request.POST.get('numDuracion')
        fecha_salida = request.POST.get('fecha_salida')
        fecha_retorno = request.POST.get('fecha_retorno')
        precio = request.POST.get('numPrecio')
        tren_id = request.POST.get('selectTren')
        horario_salida = request.POST.get('horarioSalida')
        horario_retorno = request.POST.get('horarioRetorno')

        tren = Tren.objects.get(id=tren_id)

        if origen == destino:
            messages.error(request, "El origen y destino deben ser diferentes.")
            return render(request, 'rutas/ruta_form.html')

        if fecha_salida == fecha_retorno:
            messages.error(request, "Los días de salida y retorno deben ser diferentes.")
            return render(request, 'rutas/ruta_form.html')
        
        nueva_ruta_salida = Ruta(
            origen=origen,
            destino=destino,
            duracion=duracion,
            fecha_salida=fecha_salida,
            hora_salida=horario_salida,
            precio=precio,
            tren=tren,
        )
        nueva_ruta_salida.save()
        
        nueva_ruta_retorno = Ruta(
            origen=destino,
            destino=origen,
            duracion=duracion,
            fecha_salida=fecha_retorno,
            hora_salida=horario_retorno,
            precio=precio,
            tren=tren,
        )
        nueva_ruta_retorno.save()

        return redirect('ruta_lista')  # Cambia 'ruta_lista' por la URL que quieras para redirigir

    trenes = Tren.objects.all()

    return render(request, 'ruta_registrar.html', {'trenes': trenes})

#Editar Ruta
def rutaEdicion(request, id):
    trenes_activos = Tren.objects.filter(estado=True)
    ruta = Ruta.objects.get(id=id)
    
    data = {
        'ruta': ruta,
        'trenes': trenes_activos
    }
    return render(request, 'rutas/ruta_editar.html', data)

def editarRuta(request):
    id = request.POST['id']
    fecha_salida = request.POST.get('fecha_salida', None).title()
    precio = request.POST['numPrecio']
    tren = request.POST['selectTren']
    hora_salida = request.POST.get('horarioSalida', None)
    horario_retorno = request.POST.get('horarioRetorno', None)

    ruta = Ruta.objects.get(id=id)
    tren = Tren.objects.get(id=tren)
    
    if ruta.fecha_salida and ruta.hora_salida != "Null" and fecha_salida and hora_salida:
        ruta.fecha_salida = fecha_salida
        ruta.hora_salida = hora_salida
    ruta.precio = precio
    ruta.tren = tren
    ruta.save()
    
    return redirect('ruta_lista')

def eliminarRuta (request, id):
    ruta = Ruta.objects.get(id=id)
    ruta.delete()
    return redirect('rutas_lista')

def verificarDisponibilidadAsiento(ruta_id):
    asientos_disponibles = Asiento.objects.filter(ruta_id=ruta_id, estado=1).count()
    return asientos_disponibles

def rutaLista(request):
    rutas = Ruta.objects.all()
    
    data = {
        'rutas': rutas,  # El queryset de rutas
    }
    
    return render(request, 'rutas/ruta_list.html', data)
    
def rutas_disponibles(request):
    query = request.GET.get('searchRuta', '')
    rutas = Ruta.objects.filter(tren__estado=True).select_related('tren')

    # Obtener la fecha y hora actual
    ahora = timezone.now()

    # Filtrar las rutas cuyo fecha_salida y hora_salida no sean posteriores a la fecha y hora actuales
    rutas = rutas.filter(
        Q(fecha_salida__gt=ahora.date()) |  # Las rutas cuya fecha_salida ya pasó
        Q(fecha_salida=ahora.date(), hora_salida__gte=ahora.time())  # Si la fecha es hoy, comprobamos la hora de salida
    )
    
    # Si hay una búsqueda, filtramos las rutas
    if query:
        query = query.title()
        rutas = rutas.filter(
            models.Q(origen__icontains=query) | models.Q(destino__icontains=query)
        )
        
    # Añadir asientos disponibles a cada ruta usando verificarDisponibilidad
    rutas_disponibles = []
    for ruta in rutas:
        asientos_disponibles = verificarDisponibilidad(ruta.id)
        rutas_disponibles.append({
            'ruta': ruta,
            'asientos_disponibles': asientos_disponibles
        })

    data = {
        'rutas_disponibles': rutas_disponibles
    }

    return render(request, 'rutas/rutas_disponibles.html', data)