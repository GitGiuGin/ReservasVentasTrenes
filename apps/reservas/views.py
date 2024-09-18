from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Reserva
from apps.asientos.models import Asiento

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
    if request.method == 'POST':
        fechaReserva = request.POST.get('txtFechaReserva')
        id_asientos_seleccionados = request.POST.getlist('asientos_seleccionados') # ['1', '2', '3']
        ruta_id = request.POST.get('txtRutaId')
        ruta_origen = request.POST.get('txtOrigen')
        ruta_destino = request.POST.get('txtDestino')
        ruta_precio = request.POST.get('txtPrecioAsiento')
        tren = request.POST.get('txtTren')
        
        # Filtra los asientos utilizando los IDs obtenidos
        asientos = Asiento.objects.filter(id__in=id_asientos_seleccionados, estado=True, ruta_id=ruta_id)
        total_asientos = Asiento.objects.filter(id__in=id_asientos_seleccionados, estado=True, ruta_id=ruta_id).count()
        precio_total = total_asientos * float(ruta_precio)
        precio_total_formateado = "{:.2f}".format(precio_total)
        
        # Prepara los datos para renderizar
        data = {
            'asientos_seleccionados': asientos, #Datos de los asientos
            'ruta_id': ruta_id,
            'fechaReserva': fechaReserva,
            'ruta_origen': ruta_origen,
            'ruta_destino': ruta_destino,
            'tren': tren,
            'ruta_precio': ruta_precio,
            'total_asientos': total_asientos,
            'precio_total': precio_total_formateado
        }
        
        return render(request, 'reservas/reserva_form.html', data)
    
    return render(request, 'reservas/reserva_form.html')