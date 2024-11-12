from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.views.generic import ListView
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.mail import EmailMessage
from django.conf import settings
from django.db.models import Count
from django.db.models import Q
from django.template.loader import render_to_string
from django.utils import timezone
from .models import Cliente
from weasyprint import HTML
from django.http import HttpResponse
from apps.reservas.models import Reserva

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
    search_query = request.GET.get("searchReserva", "")  # Obtén el valor de búsqueda
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
    
    today = timezone.now().date()
    
    # Consulta adaptada
    reservas = Reserva.objects.filter(
        cliente__id=usuario.id
    ).annotate(
        asientos_reservados=Count('reservas_asientos')  # Contamos el número de asientos reservados
    ).select_related('ruta', 'ruta__tren').filter(
        Q(ruta__origen__icontains=search_query) |
        Q(ruta__destino__icontains=search_query) |
        Q(fecha_reserva__icontains=search_query) |
        Q(estado__icontains=search_query)           
    ).values(
        'ruta__id',
        'ruta__origen',
        'ruta__destino',
        'ruta__fecha_salida',
        'ruta__hora_salida',
        'fecha_reserva',
        'estado',
        'id',
        'ruta__tren__nombre',
        'asientos_reservados'
    ).order_by('id')
    
    data = {
        "usuario": usuario,
        "reservas": reservas,
        'today': today
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
    usuario = request.user
    reserva = get_object_or_404(Reserva, id=reserva_id)
    asientos_reservados = reserva.reservas_asientos.all()
    
    data = {
        'usuario': usuario,
        'reserva': reserva,
        'asientos_reservados': asientos_reservados,
    }

    if request.GET.get('generar_pdf') == 'True':
        html_string = render_to_string('clientes/ticket.html', data)
        pdf_file = HTML(string=html_string).write_pdf()

        response = HttpResponse(pdf_file, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="Ticket.pdf"'
        return response

    return render(request, 'clientes/detalle_reserva.html', data)

@login_required
def enviar_ticket_por_email(request, reserva_id):
    usuario = request.user
    reserva = get_object_or_404(Reserva, id=reserva_id)
    asientos_reservados = reserva.reservas_asientos.all()

    # Datos para la plantilla del PDF
    data = {
        'usuario': usuario,
        'reserva': reserva,
        'asientos_reservados': asientos_reservados,
    }

    # Generar el PDF con los datos
    html_string = render_to_string('clientes/ticket.html', data)
    pdf_file = HTML(string=html_string).write_pdf()

    # Crear el correo
    email = EmailMessage(
        subject="Tu Reserva - Ticket PDF",
        body="Adjunto encontrarás el ticket de tu reserva.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[usuario.correo]  # El correo del usuario que ha iniciado sesión
    )

    # Adjuntar el archivo PDF
    email.attach('Ticket.pdf', pdf_file, 'application/pdf')

    # Enviar el correo
    email.send()

    # Redirigir o devolver una respuesta después de enviar el correo
    return HttpResponse("El ticket ha sido enviado a tu correo electrónico.")