from django.shortcuts import render, redirect
from django.db import models
from django.views.generic import ListView
from .models import Ruta
from apps.trenes.models import Tren

# Create your views here.

def index (request):
    pass

def rutaForm(request):
    trenes_activos = Tren.objects.filter(estado=True)
    return render(request, 'rutas/ruta_form.html', {'trenes': trenes_activos})

def registrarRuta(request):
    if request.method == 'POST':
        origen = request.POST.get('txtOrigen')
        destino = request.POST.get('txtDestino')
        duracion = request.POST.get('numDuracion')
        dia_salida = request.POST.get('selectDiaSalida')
        dia_retorno = request.POST.get('selectDiaRetorno')
        precio = request.POST.get('numPrecio')
        tren_id = request.POST.get('selectTren')

        dias_disponibles = ', '.join(request.POST.getlist('selectDiasDisponibles'))  # Maneja la selección múltiple

        tren = Tren.objects.get(id=tren_id) if tren_id else None

        nueva_ruta = Ruta(
            origen=origen,
            destino=destino,
            duracion=duracion,
            dia_salida=dia_salida,
            dia_retorno=dia_retorno,
            precio=precio,
            tren=tren,
            dias_disponibles=dias_disponibles
        )
        nueva_ruta.save()

        return redirect('ruta_lista')  # Cambia 'ruta_exito' por la URL que quieras para redirigir

    trenes = Tren.objects.all()

    return render(request, 'ruta_registrar.html', {'trenes': trenes})

#Editar Ruta
def rutaEdicion(request, id):
    ruta = Ruta.objects.get(id=id)
    data = {
        'ruta': ruta
    }
    return render(request, 'rutas/ruta_editar.html', data)

def editarRuta(request):
    id = request.POST['id']
    origen = request.POST['txtOrigen']
    destino = request.POST['txtDestino']
    precio = request.POST['txtPrecio']

    ruta = Ruta.objects.get(id=id)
    ruta.origen = origen
    ruta.destino = destino
    ruta.precio = precio
    ruta.save()
    
    return redirect('ruta_lista')

def eliminarRuta (request, id):
    ruta = Ruta.objects.get(id=id)
    ruta.delete()
    return redirect('rutas_lista')

class RutaListView (ListView):
    model = Ruta
    template_name = 'rutas/ruta_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gesion de Rutas'
        return context
    
def rutas_disponibles(request):
    query = request.GET.get('searchRuta', '')
    rutas = Ruta.objects.filter(tren__estado=True).select_related('tren')

    if query:
        rutas = rutas.filter(
            models.Q(origen__icontains=query) | models.Q(destino__icontains=query)
        )
    
    return render(request, 'rutas/rutas_disponibles.html', {'rutas': rutas})