from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Ruta

# Create your views here.

def index (request):
    pass

def rutaForm(request):
    return render(request, 'rutas/ruta_form.html')

def registrarRuta (request):
    origen = request.POST['txtOrigen']
    destino = request.POST['txtDestino']
    duracion = request.POST['numDuracion']
    precio = request.POST['txtPrecio']

    tren = Ruta.objects.create(
        origen=origen,
        destino=destino,
        duracion=duracion,
        precio=precio
        )
    return redirect('rutas_lista')

def editarRuta(request):
    return render(request, 'rutas/ruta_editar.html')

def eliminarRuta (request, id):
    tren = Ruta.objects.get(id=id)
    tren.delete()
    return redirect('rutas_lista')

class RutaListView (ListView):
    model = Ruta
    template_name = 'rutas/ruta_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gesion de Rutas'
        return context