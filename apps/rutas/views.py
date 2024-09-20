from django.shortcuts import render, redirect
from django.db import models
from django.views.generic import ListView
from django.contrib import messages
from .models import Ruta
from apps.trenes.models import Tren
from apps.asientos.models import Asiento
from datetime import datetime
from django import forms

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
        dia_salida = request.POST.get('selectDiaSalida').title()
        dia_retorno = request.POST.get('selectDiaRetorno').title()
        precio = request.POST.get('numPrecio')
        tren_id = request.POST.get('selectTren')
        horario_salida = request.POST['horarioSalida']
        horario_retorno = request.POST['horarioRetorno']

        tren = Tren.objects.get(id=tren_id)

        if origen == destino:
            messages.error(request, "El origen y destino deben ser diferentes.")
            return render(request, 'rutas/ruta_form.html')

        if dia_salida == dia_retorno:
            messages.error(request, "Los días de salida y retorno deben ser diferentes.")
            return render(request, 'rutas/ruta_form.html')
        
        nueva_ruta_salida = Ruta(
            origen=origen,
            destino=destino,
            duracion=duracion,
            dia_salida=dia_salida,
            horario_salida=horario_salida,
            precio=precio,
            tren=tren,
        )
        nueva_ruta_salida.save()
        
        nueva_ruta_retorno = Ruta(
            origen=destino,
            destino=origen,
            duracion=duracion,
            dia_retorno=dia_retorno,
            horario_retorno=horario_retorno,
            precio=precio,
            tren=tren,
        )
        nueva_ruta_retorno.save()

        # Obtener el ID de la nueva ruta
        ruta_id_salida = nueva_ruta_salida.id
        asientos_salida = [
            Asiento(estado=1, numero_asiento="1A", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="1B", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="1C", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="1D", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="2A", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="2B", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="2C", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="2D", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="3A", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="3B", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="3C", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="3D", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="4A", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="4B", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="4C", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="4D", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="5A", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="5B", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="5C", ruta_id=ruta_id_salida),
            Asiento(estado=1, numero_asiento="5D", ruta_id=ruta_id_salida),
        ]
        Asiento.objects.bulk_create(asientos_salida)
        
        ruta_id_retorno = nueva_ruta_retorno.id
        asientos_retorno = [
            Asiento(estado=1, numero_asiento="1A", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="1B", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="1C", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="1D", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="2A", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="2B", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="2C", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="2D", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="3A", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="3B", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="3C", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="3D", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="4A", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="4B", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="4C", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="4D", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="5A", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="5B", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="5C", ruta_id=ruta_id_retorno),
            Asiento(estado=1, numero_asiento="5D", ruta_id=ruta_id_retorno),
        ]
        Asiento.objects.bulk_create(asientos_retorno)

        return redirect('ruta_lista')  # Cambia 'ruta_exito' por la URL que quieras para redirigir

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
    dia_salida = request.POST.get('selectDiaSalida', None).title()
    dia_retorno = request.POST.get('selectDiaRetorno', None).title()
    precio = request.POST['numPrecio']
    tren = request.POST['selectTren']
    horario_salida = request.POST.get('horarioSalida', None).title()
    horario_retorno = request.POST.get('horarioRetorno', None) .title()

    ruta = Ruta.objects.get(id=id)
    tren = Tren.objects.get(id=tren)
    
    if ruta.dia_salida and ruta.horario_salida != "Null" and dia_salida and horario_salida:
        ruta.dia_salida = dia_salida
        ruta.horario_salida = horario_salida
    if ruta.dia_retorno and ruta.horario_retorno != "Null" and dia_retorno and horario_retorno:
        ruta.dia_retorno = dia_retorno
        ruta.horario_retorno = horario_retorno
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

    if query:
        query = query.title()
        rutas = rutas.filter(
            models.Q(origen__icontains=query) | models.Q(destino__icontains=query)
        )
    
    return render(request, 'rutas/rutas_disponibles.html', {'rutas': rutas})