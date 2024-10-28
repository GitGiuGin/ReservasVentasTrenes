from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Reserva
from apps.asientos.models import Asiento
from apps.rutas.models import Ruta
from apps.clientes.models import Cliente
from apps.reservas.models import Reserva, ReservaAsiento
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
    ruta_id = request.POST.get('txtIdRuta')
    id_usuario = request.POST.get('id_usuario')
    usuario_especifico = Cliente.objects.get(id = id_usuario)
    ruta_especifica = Ruta.objects.get(id=int(ruta_id))
    
    reserva = Reserva.objects.create(
            fecha_reserva=fecha_formateada,
            estado=True, 
            ruta=ruta_especifica,
            cliente=usuario_especifico
        )   
    
    # Guardar los IDs de los asientos como objetos de la clase ReservaAsiento
    for asiento_id in id_asientos_reservados:
        asiento = Asiento.objects.get(id=int(asiento_id))
        ReservaAsiento.objects.create(
            reserva=reserva,
            asiento=asiento,
            estado=False  # Estado en ReservaAsiento, asumiendo que 'False' significa que el asiento está reservado
        )
    
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
        ruta_id = request.POST.get('txtRutaId')
        ruta_origen = request.POST.get('txtOrigen').title()
        ruta_destino = request.POST.get('txtDestino').title()
        ruta_precio = request.POST.get('txtPrecioAsiento')
        tren = request.POST.get('txtTren')
        tren_id = request.POST.get('txtIdTren')
        id_asientos_seleccionados = request.POST.getlist('asientos_seleccionados') # ['1', '2', '3']
        
        # Validar que la ruta existe
        try:
            ruta = Ruta.objects.get(id=ruta_id)
        except Ruta.DoesNotExist:
            # Manejo del error si la ruta no existe
            return render(request, 'reservas/reserva_form.html', {'error': 'Ruta no encontrada'})
        
        # Filtra los asientos utilizando los IDs obtenidos
        asientos_ocupados  = ReservaAsiento.objects.filter(
            reserva__ruta=ruta,
            asiento__id__in=id_asientos_seleccionados, 
            estado=False
        )
        ids_ocupados = [str(asiento.asiento.id) for asiento in asientos_ocupados]
        asientos_no_ocupados = [
            id_asiento for id_asiento in id_asientos_seleccionados if id_asiento not in ids_ocupados
        ]
        asientos = Asiento.objects.filter(id__in = asientos_no_ocupados)
        
        print(f"Ruta ID: {ruta_id}")
        print(f"Asientos seleccionados: {id_asientos_seleccionados}")
        print(f"Asientos Ocupados: {asientos_ocupados}")
        print(f"Ids Ocupados: {ids_ocupados}")
        print(f"Asientos No Ocupados: {asientos_no_ocupados}")
        
        total_asientos = len(asientos_no_ocupados)  # Esto debería ser 2 para asientos 5 y 6
        total_reserva = precio_total(total_asientos, ruta_precio)  # Calcula el total de la reserva
        
        # Prepara los datos para renderizar
        data = {
            'id_usuario' : id_usuario,
            'nombres' : nombres,
            'apellido_paterno' : apellido_paterno,
            'apellido_materno' : apellido_materno,
            'correo' : correo,
            'telefono' : telefono,
            'fechaReserva': fechaReserva,
            'ruta_id': ruta_id,
            'ruta_origen': ruta_origen,
            'ruta_destino': ruta_destino,
            'ruta_precio': ruta_precio,
            'tren': tren,
            'tren_id': tren_id,
            'asientos_seleccionados': asientos,
            'total_asientos': total_asientos,
            'total_reserva': total_reserva,
        }
        
        return render(request, 'reservas/reserva_form.html', data)
    
    return render(request, 'reservas/reserva_form.html')