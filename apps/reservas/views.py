from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Reserva

# Create your views here:
def index(request):
    return render(request, 'reservas/reserva_index.html')  # Renderiza una plantilla llamada 'index.html'

#Creacion de cliente
def reservaForm(request):
    return render(request, 'reservas/reserva_form.html')

def registrarReserva(request):
    nombre = request.POST['txtNombre']
    apellido_paterno = request.POST['txtApellidoPaterno']
    apellido_materno = request.POST['txtApellidoMaterno']
    correo = request.POST['txtCorreo']
    telefono = request.POST['txtTelefono']
    direccion = request.POST['txtDireccion']
    contrasena = request.POST['txtContraseña']

    reserva = Reserva.objects.create(
        nombres=nombre, 
        apellido_paterno=apellido_paterno,
        apellido_materno=apellido_materno,
        correo=correo,
        telefono=telefono,
        direccion=direccion,
        contraseña=contrasena
        )
    return redirect('reserva_lista')

#Editar Cliente
def reservaEditar(request):
    return render(request, 'reservas/reserva_editar.html')

#Eliminar Cliente
def eliminarReserva (request, id):
    cliente = Reserva.objects.get(id=id)
    cliente.delete()
    return redirect('ruta_lista')

#Consultar cliente
class ReservaListView (ListView):
    model = Reserva
    template_name = 'reservas/reserva_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestion de Reservas'
        return context
    
def confirmarFormReserva(request):
    return render(request, 'reservas/reserva_form.html')