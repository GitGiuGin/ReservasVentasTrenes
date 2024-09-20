from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from .models import Cliente

# Create your views here:
def index(request):
    return render(request, 'clientes/clientes_index.html')  # Renderiza una plantilla llamada 'index.html'

#Creacion de cliente
def clientesForm(request):
    return render(request, 'clientes/cliente_form.html')

def registrarCliente(request):
    nombre = request.POST.get('txtNombre').title()
    apellido_paterno = request.POST.get('txtApellidoPaterno').title()
    apellido_materno = request.POST.get('txtApellidoMaterno').title()
    correo = request.POST.get('txtCorreo')
    telefono = request.POST.get('txtTelefono')
    direccion = request.POST.get('txtDireccion').title()
    contrasena = request.POST.get('txtContraseña')
    contrasena_repetida = request.POST.get('txtConfContraseña')

    if contrasena != contrasena_repetida:
            messages.error(request, "Las contraseñas no coinciden.")
            return render(request, 'clientes/cliente_form.html')

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

#Editar Cliente
def clientesEdicion(request, id):
    cliente = Cliente.objects.get(id=id)
    data = {
        'cliente': cliente
    }
    return render(request, 'clientes/cliente_editar.html', data)

def editarCliente(request):
    id = request.POST['id']
    correo = request.POST['txtCorreo']
    telefono = request.POST['txtTelefono']
    direccion = request.POST['txtDireccion'].title()
    estado = request

    cliente = Cliente.objects.get(id=id)
    cliente.correo = correo
    cliente.telefono = telefono
    cliente.direccion = direccion
    cliente.save()
    
    return redirect('clientes_lista')

#Consultar cliente
class ClienteListView (ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'object_list'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_cliente = self.request.GET.get('searchCliente', '')

        if search_cliente:
            search_cliente = search_cliente.title()
            # Filtramos por nombre, apellido paterno y apellido materno
            queryset = queryset.filter(
                nombres__icontains=search_cliente
            ) | queryset.filter(
                apellido_paterno__icontains=search_cliente
            ) | queryset.filter(
                apellido_materno__icontains=search_cliente
            )
        
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gesion de Clientes'
        return context
