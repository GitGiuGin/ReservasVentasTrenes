from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Tren

# Create your views here:
def index(request):
    return render(request, 'trenes/tren_index.html')  # Renderiza una plantilla llamada 'index.html'

def trenesNew(request):
    return render(request, 'trenes/tren_new.html')

def trenesEditar(request):
    return render(request, 'trenes/tren_editar.html')

def trenesList(request):
    listarTrenes = Tren.objects.all()

    data = {
        'titulo': 'Gestion Trenes',
        'trenes': listarTrenes
    }

class TrenListView (ListView):
    model = Tren
    template_name = 'trenes/tren_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gesion de Trenes'
        return context
    
def eliminarTren (request, id):
    tren = Tren.objects.get(id=id)
    tren.delete()
    return redirect('trenes_lista')

def registrarTren (request):
    nombre = request.POST['txtNombre']
    capacidad = request.POST['txtCapacidad']

    tren = Tren.objects.create(
        nombre=nombre, 
        capacidad=capacidad,
        )
    return redirect('trenes_lista')