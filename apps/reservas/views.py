from django.shortcuts import render, redirect, get_object_or_404
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
def nuevaReserva(request):
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
    
    return redirect('mi_cuenta')

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

def editarReserva(request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    asientos_reservados = reserva.reservas_asientos.all()
    
    lista_asientos_reservados = []
    for reserva_asiento in asientos_reservados:
        id_reserva_asiento = reserva_asiento.id
        id_asiento = reserva_asiento.asiento.id
        numero_asiento = reserva_asiento.asiento.numero_asiento
        lista_asientos_reservados.append((id_reserva_asiento, id_asiento, numero_asiento))
    
    id_asientos_reservados = request.POST.getlist('asientos_reservados')
    
    eliminar_registros = ReservaAsiento.objects.filter(reserva_id=reserva_id).delete()
    
    # Guardar los IDs de los asientos como objetos de la clase ReservaAsiento
    for asiento_id in id_asientos_reservados:
        asiento = Asiento.objects.get(id=int(asiento_id))
        ReservaAsiento.objects.create(
            reserva=reserva,
            asiento=asiento,
            estado=False  # Estado en ReservaAsiento, asumiendo que 'False' significa que el asiento está reservado
        )
    
    return redirect('mi_cuenta')

def confEditarReserva(request, reserva_id):
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
        reserva = get_object_or_404(Reserva, id=reserva_id)
        id_reserva = reserva.id
        asientos_reservados = reserva.reservas_asientos.all()
    
        # Crear una lista con los ID y numero_asiento
        # Crear una lista con los ID y numero_asiento de los asientos reservados
        lista_asientos_reservados = [
            (reserva_asiento.id, reserva_asiento.asiento.id, reserva_asiento.asiento.numero_asiento)
            for reserva_asiento in asientos_reservados
        ]

        # Validar que la ruta existe
        ruta = get_object_or_404(Ruta, id=ruta_id)

        # Filtrar los asientos ocupados por la ruta
        asientos_ocupados = ReservaAsiento.objects.filter(
            reserva__ruta=ruta,
            estado=False  # Esto asume que 'estado' False significa que el asiento está ocupado
        ).exclude(reserva__id=reserva_id)

        # Crear un conjunto de IDs ocupados y reservados
        ids_ocupados = [str(asiento.asiento.id) for asiento in asientos_ocupados]
        asientos_seleccionados = [
            id_asiento for id_asiento in id_asientos_seleccionados if id_asiento not in ids_ocupados
        ]

        asientos = Asiento.objects.filter(id__in = asientos_seleccionados)
    
        total_asientos = len(asientos_seleccionados)  # Esto debería ser 2 para asientos 5 y 6
        total_reserva_antigua = precio_total(len(lista_asientos_reservados), ruta_precio)
        total_reserva = precio_total(total_asientos, ruta_precio)  # Calcula el total de la reserva
        
        # Prepara los datos para renderizar
        data = {
            'id_reserva': id_reserva,
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
            'lista_asientos_reservados': lista_asientos_reservados,
            'asientos_seleccionados': asientos,
            'total_asientos': total_asientos,
            'total_reserva': total_reserva,
        }
        
        return render(request, 'reservas/reserva_formEdit.html', data)
    
    return render(request, 'reservas/reserva_formEdit.html')

def cancelar_reserva (request, reserva_id):
    reserva = get_object_or_404(Reserva, id=reserva_id)
    reserva.delete()
    eliminar_registros = ReservaAsiento.objects.filter(reserva_id=reserva_id)
    eliminar_registros.delete()
    
    return redirect('mi_cuenta')