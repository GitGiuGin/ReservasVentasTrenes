from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Reserva
from apps.asientos.models import Asiento
from apps.trenes.models import Tren
from apps.clientes.models import Cliente
from datetime import datetime

def modificarFecha(fecha_reserva):
    fecha_reserva = datetime.strptime(fecha_reserva, "%d/%m/%Y")
    fecha_formateada = fecha_reserva.date()
    return fecha_formateada

#Creacion de cliente
def reservaForm(request):
    id_asientos_reservados = request.POST.getlist('asientos_reservados')
    fecha_reserva = request.POST.get('txtFechaReserva')
    fecha_formateada = modificarFecha(fecha_reserva)
    tren_id = request.POST.get('txtiDTren')
    id_usuario = request.POST.get('id_usuario')
    
    tren_especifico = Tren.objects.get(id=int(tren_id))
    usuario_especifico = Cliente.objects.get(id = id_usuario)
    
    reserva = Reserva.objects.create(
        fecha_reserva = fecha_formateada,
        estado = True,
        tren = tren_especifico,
        cliente = usuario_especifico
    )   
    
    reserva_id = reserva.id
    Asiento.objects.filter(id__in=id_asientos_reservados).update(estado=False, reserva_id=reserva_id)
    
    return render(request, 'reservas/reserva_list.html')

def registrarReserva(request):
    nombre = request.POST['txtNombre'].title()
    apellido_paterno = request.POST['txtApellidoPaterno'].title()
    apellido_materno = request.POST['txtApellidoMaterno'].title()
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
    reserva = Reserva.objects.get(id=id)
    reserva.estado = None
    return redirect('ruta_lista')

#Consultar cliente
class ReservaListView (ListView):
    model = Reserva
    template_name = 'reservas/reserva_list.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = 'Gestion de Reservas'
        return context

def precio_total(total_asientos, ruta_precio):
    precio_total = total_asientos * float(ruta_precio)
    precio_total_formateado = "{:.2f}".format(precio_total)
    return precio_total_formateado

def confirmarFormReserva(request):
    if request.method == 'POST':
        id_usuario = request.POST.get('id_usuario')
        nombres = request.POST.get('txtNombres')
        apellido_paterno = request.POST.get('txtApellidoPaterno')
        apellido_materno = request.POST.get('txtApellidoMaterno')
        correo = request.POST.get('txtCorreo')
        telefono = request.POST.get('txtTelefono')
        fechaReserva = request.POST.get('txtFechaReserva')
        id_asientos_seleccionados = request.POST.getlist('asientos_seleccionados') # ['1', '2', '3']
        ruta_id = request.POST.get('txtRutaId')
        ruta_origen = request.POST.get('txtOrigen').title()
        ruta_destino = request.POST.get('txtDestino').title()
        ruta_precio = request.POST.get('txtPrecioAsiento')
        tren = request.POST.get('txtTren')
        tren_id = request.POST.get('txtIdTren')
        
        # Filtra los asientos utilizando los IDs obtenidos
        asientos = Asiento.objects.filter(id__in=id_asientos_seleccionados, estado=True, ruta_id=ruta_id)
        total_asientos = asientos.count()
        total_reserva = precio_total(total_asientos, ruta_precio)
        
        # Prepara los datos para renderizar
        data = {
            'id_usuario' : id_usuario,
            'nombres' : nombres,
            'apellido_paterno' : apellido_paterno,
            'apellido_materno' : apellido_materno,
            'correo' : correo,
            'telefono' : telefono,
            'asientos_seleccionados': asientos, #Datos de los asientos
            'ruta_id': ruta_id,
            'fechaReserva': fechaReserva,
            'ruta_origen': ruta_origen,
            'ruta_destino': ruta_destino,
            'tren': tren,
            'tren_id': tren_id,
            'ruta_precio': ruta_precio,
            'total_asientos': total_asientos,
            'total_reserva': total_reserva
        }
        
        return render(request, 'reservas/reserva_form.html', data)
    
    return render(request, 'reservas/reserva_form.html')