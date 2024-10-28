from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.contrib import messages
from django.db.models import Count
from .models import Cliente
from apps.reservas.models import Reserva
from apps.asientos.models import Asiento
from apps.trenes.models import Tren
from apps.rutas.models import Ruta

#Creacion de cliente
def clientesForm(request):
    return render(request, 'clientes/cliente_form.html')

def registro_cliente_desde_login(request):
    if request.method == 'POST':
        return registrarCliente(request, desde_login=True)  # Pasar el parámetro
    return render(request, 'clientes/cliente_form.html')

def registrarCliente(request, desde_login=False):
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

    cliente = Cliente(
        nombres=nombre,
        apellido_paterno=apellido_paterno,
        apellido_materno=apellido_materno,
        correo=correo,
        telefono=telefono,
        direccion=direccion,
        is_active=True,
        is_staff=False,
        is_superuser=False
    )
    cliente.set_password(contrasena)
    cliente.save()
    
    if request.user.is_staff:
        return redirect('clientes_lista')  
    elif desde_login:
        return redirect('login')  
    return redirect('clientes_lista')

#Editar Cliente
def clientesEdicion(request, id, next):
    cliente = Cliente.objects.get(id=id)
    data = {
        'cliente': cliente,
        'next': next
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
    
    next_url = request.POST.get('next', 'clientes_lista')
    
    return redirect(next_url)

#Consultar cliente
class ClienteListView (ListView):
    model = Cliente
    template_name = 'clientes/cliente_list.html'
    context_object_name = 'object_list'
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search_cliente = self.request.GET.get('searchCliente', '')
        
        queryset = queryset.filter(tipo_usuario='cliente')

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

def custom_login_view(request):
    if request.method == 'POST':
        correo = request.POST.get('correo')
        contraseña = request.POST.get('contraseña') 
        
        user = authenticate(request, username=correo, password=contraseña)
        
        if user is not None:
            login(request, user)
            print(f"Usuario autenticado: {user} con tipo_usuario: {user.tipo_usuario}")
            
            next_url = request.GET.get('next')
            
            if next_url:
                return redirect(next_url)
            else:
                if user.is_staff or user.tipo_usuario == 'administrador':
                    return redirect('base')
                else:
                    return redirect('base')
        else:
            messages.error(request, 'Correo o contraseña incorrectos.')
    
    return render(request, 'clientes/login.html')

@login_required
def perfil_usuario(request):
    usuario = request.user
    if request.method == "POST":
        contraseña = request.POST.get("txtContraseña")
        confirmar_contraseña = request.POST.get("txtConfContraseña")
        
        if contraseña and confirmar_contraseña:
            if contraseña == confirmar_contraseña:
                # Cambia la contraseña del usuario
                usuario.password = make_password(contraseña)
                usuario.save()
            else:
                messages.error(request, "Las contraseñas no coinciden. Intenta nuevamente.")
        else:
            messages.error(request, "Por favor, completa todos los campos.")
        
        return redirect("mi_cuenta")  
    
    # Consulta adaptada
    reservas = Reserva.objects.filter(cliente__id=usuario.id).annotate(
        asientos_disponibles=Count('reservas_asientos__estado')  # Contamos el número de asientos reservados
    ).select_related('ruta', 'ruta__tren').values(
        'ruta__origen',        # Ruta origen
        'ruta__destino',       # Ruta destino
        'ruta__fecha_salida',    # Día de salida
        'ruta__hora_salida', # Hora de salida
        'fecha_reserva',       # Fecha de reserva
        'estado',              # Estado de la reserva
        'id',                  # ID de la reserva
        'ruta__tren__nombre',  # Nombre del tren
    ).order_by('id')  # Ordenar por el ID de la reserva
    
    data = {
        "usuario": usuario,
        "reservas": reservas
    }
    return render(request, "clientes/perfil.html", data)

def reservas_usuario (request):
    usuario = request.user
    data = {
        "usuario" : usuario
    }
    return render (request, "clientes/mis_reservas.html", data)

@login_required
def detalle_reserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)  # Obtener la reserva

    # Acceder al tren desde la reserva
    tren = reserva.ruta.tren  # Asegúrate de que la reserva tiene un campo `ruta`

    # Ahora puedes acceder a las rutas relacionadas con este tren
    rutas = tren.rutas.all()  # Esto obtiene todas las rutas asociadas a este tren

    # Continúa con la lógica de tu vista
    context = {
        'reserva': reserva,
        'tren': tren,
        'rutas': rutas,
        # Otros contextos que necesites
    }

    return render(request, 'tu_template.html', context)