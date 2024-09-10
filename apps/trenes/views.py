from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Tren

# Create your views here:
def index(request):
    return render(request, 'trenes/tren_index.html')  # Renderiza una plantilla llamada 'index.html'

def trenesForm(request):
    return render(request, 'trenes/tren_form.html')

def registrarTren (request):
    nombre = request.POST['txtNombre']

    tren = Tren.objects.create(
        nombre=nombre, 
        )
    return redirect('trenes_lista')

#Editar tren
def trenEdicion(request, id):
    tren = Tren.objects.get(id=id)
    data = {
        'tren': tren
    }
    return render(request, 'trenes/tren_editar.html', data)

def editarTren(request):
    id = request.POST['id']
    estado = request.POST['txtEstado']

    tren = Tren.objects.get(id=id)
    tren.estado = estado
    tren.save()
    
    return redirect('trenes_lista')

class TrenListView (ListView):
    model = Tren
    template_name = 'trenes/tren_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gesion de Trenes'
        return context

def activarTren():
    pass

def desactivarTren():
    pass
#def trenesList(request):
#    listarTrenes = Tren.objects.all()
#
#    data = {
#        'titulo': 'Gestion Trenes',
#        'trenes': listarTrenes
#    }