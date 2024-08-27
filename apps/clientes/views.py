from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Cliente

# Create your views here:
def index(request):
    return render(request, 'clientes/clientes_index.html')  # Renderiza una plantilla llamada 'index.html'

def clientesNew(request):
    return render(request, 'clientes/cliente_new.html')

def clientesEditar(request):
    return render(request, 'clientes/cliente_editar.html')

def clientesList(request):
    listarClientes = Cliente.objects.all()

    data = {
        'titulo': 'Gestion clientes',
        'clientes': listarClientes
    }

class ClienteListView (ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gesion de Clientes'
        return context
    
def eliminarCliente (request, id):
    cliente = Cliente.objects.get(id=id)
    cliente.delete()
    return redirect('clientes_lista')

def registrarCliente(request):
    nombre = request.POST['txtNombre']
    apellido_paterno = request.POST['txtApellidoPaterno']
    apellido_materno = request.POST['txtApellidoMaterno']
    correo = request.POST['txtCorreo']
    telefono = request.POST['txtTelefono']
    direccion = request.POST['txtDireccion']
    contrasena = request.POST['txtContraseña']

    cliente = Cliente.objects.create(
        nombres=nombre, 
        apellido_paterno=apellido_paterno,
        apellido_materno=apellido_materno,
        correo=correo,
        telefono=telefono,
        direccion=direccion,
        contraseña=contrasena
        )
    return redirect('clientes_lista')