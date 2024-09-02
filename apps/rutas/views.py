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