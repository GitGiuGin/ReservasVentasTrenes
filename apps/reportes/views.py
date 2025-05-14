from django.shortcuts import render, get_object_or_404
from django.template.loader import render_to_string
from django.http import HttpResponse
from django.db.models import Count, Sum, F, Q
from apps.clientes.models import Cliente
from apps.rutas.models import Ruta
from apps.pagos.models import Pago
from apps.reservas.models import Reserva
from datetime import datetime
from weasyprint import HTML

# Create your views here.
def reporte_clientes_pdf(request):
    clientes = Cliente.objects.filter(tipo_usuario='cliente')
    administrador = request.user
    fecha_actual = datetime.now()

    data = {
        'clientes': clientes,
        'administrador': administrador,
        'now': fecha_actual
    }
    
    html_string = render_to_string('reportes/reporte_clientes_pdf.html', data)
    pdf = HTML(string=html_string).write_pdf()

    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="reporte_clientes.pdf"'

    return response

def reporte_ventas(request):
    accion = request.GET.get('accion')
    fecha_inicio = request.GET.get('fecha_inicio')
    fecha_fin = request.GET.get('fecha_fin')
    
    # Convertir las fechas a formato DateTime si son proporcionadas
    if fecha_inicio:
        fecha_inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    if fecha_fin:
        fecha_fin = datetime.strptime(fecha_fin, "%Y-%m-%d")
        fecha_fin = fecha_fin.replace(hour=23, minute=59, second=59)

    # Filtrar los pagos según el rango de fechas
    if fecha_inicio and fecha_fin:
        resultados = Pago.objects.filter(fecha_pago__range=[fecha_inicio, fecha_fin])
    elif fecha_inicio:
        resultados = Pago.objects.filter(fecha_pago__gte=fecha_inicio)
    elif fecha_fin:
        resultados = Pago.objects.filter(fecha_pago__lte=fecha_fin)
    else:
        resultados = Pago.objects.all()  # Si no hay filtros, se muestran todos los pagos
    
    reporte = Pago.objects.select_related(
        'reserva__cliente',
        'reserva__ruta__tren',
        'reserva__ruta',
    ).annotate(
        num_asientos_reservados=Count('reserva__reservas_asientos')
    ).order_by('-fecha_pago') 
    
    # Si hay fechas de filtro, aplicamos el mismo filtro en la consulta 'reporte'
    if fecha_inicio and fecha_fin:
        reporte = reporte.filter(fecha_pago__range=[fecha_inicio, fecha_fin])
    elif fecha_inicio:
        reporte = reporte.filter(fecha_pago__gte=fecha_inicio)
    elif fecha_fin:
        reporte = reporte.filter(fecha_pago__lte=fecha_fin)
    
    total_ventas = resultados.aggregate(Sum('monto_total'))['monto_total__sum'] or 0

    # Si la acción es "descargar_pdf", generar y devolver el PDF
    if accion == 'descargar_pdf':
        administrador = request.user
        fecha_actual = datetime.now()
        context = {
            'now': fecha_actual,
            'administrador': administrador,
            'resultados': reporte,
            'fecha_inicio': fecha_inicio,
            'fecha_fin': fecha_fin,
            'total_ventas': total_ventas
        }
    
        html_string = render_to_string('reportes/reporte_ventas_pdf.html', context)
        pdf = HTML(string=html_string).write_pdf()

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'inline; filename="reporte_ventas_{fecha_inicio}_{fecha_fin}.pdf"'

        return response
    
    data = {
        'resultados': reporte,
        'fecha_inicio': fecha_inicio,
        'fecha_fin': fecha_fin,
        'total_ventas': total_ventas
    }
    return render(request, 'reportes/reporte_ventas.html', data)

def viajes_realizados(request):
    fecha_salida = request.GET.get('fecha_salida')
    cliente = request.GET.get('nombreCliente')
    
    reporte = Pago.objects.select_related(
        'reserva__cliente',
        'reserva__ruta__tren',
        'reserva__ruta',
    ).annotate(
        num_asientos_reservados=Count('reserva__reservas_asientos')
    ).order_by('-fecha_pago') 
    
    if fecha_salida:
        reporte = reporte.filter(reserva__ruta__fecha_salida__gte=fecha_salida)
    if cliente:
        reporte = reporte.filter(
            Q(reserva__cliente__nombres__icontains=cliente) |
            Q(reserva__cliente__apellido_paterno__icontains=cliente) |
            Q(reserva__cliente__apellido_materno__icontains=cliente)
        )
    
    data = {
        'reporte': reporte,
        'fecha_salida': fecha_salida,
        'cliente': cliente
    }
    
    return render(request, 'reportes/viajes_realizados.html', data)

def clientes_por_ruta(request, ruta_id):
    ruta = Ruta.objects.get(id = int(ruta_id))
    
    clientes = list(
        Reserva.objects.filter(
            Q(estado="Pagado") | Q(estado="Reservado") | Q(estado="Modificado"),
            ruta_id=ruta_id
        )
        .select_related("cliente")
        .prefetch_related("reservas_asientos__asiento")
        .values(
            nombres=F("cliente__nombres"),
            apellido_paterno=F("cliente__apellido_paterno"),
            apellido_materno=F("cliente__apellido_materno"),
            numero_asiento=F("reservas_asientos__asiento__numero_asiento"),
            reserva_estado=F("estado")
        )
        .order_by("reservas_asientos__asiento__numero_asiento")
    )
    
    data = {
        'ruta': ruta,
        'clientes': clientes
    }
    return render(request, 'reportes/clientes_por_ruta.html', data)

def clientes_por_ruta_pdf(request, ruta_id):
    administrador = request.user
    fecha_actual = datetime.now()
    ruta = Ruta.objects.get(id=ruta_id)
    
    # Filtra las reservas
    clientes = list(
        Reserva.objects.filter(
            Q(estado="Pagado") | Q(estado="Reservado") | Q(estado="Modificado"),
            ruta_id=ruta_id
        )
        .select_related("cliente")
        .prefetch_related("reservaasiento_set__asiento")
        .values(
            nombres=F("cliente__nombres"),
            apellido_paterno=F("cliente__apellido_paterno"),
            apellido_materno=F("cliente__apellido_materno"),
            numero_asiento=F("reservas_asientos__asiento__numero_asiento"),
            reserva_estado=F("estado")
        )
        .order_by("reservas_asientos__asiento__numero_asiento")
    )
    
    data = {
        'ruta': ruta,
        'clientes': clientes,
        'administrador': administrador,
        'now': fecha_actual
    }

    # Renderiza la plantilla HTML con los datos
    html_string = render_to_string('reportes/clientes_por_ruta_pdf.html', data)

    # Convierte la cadena HTML a PDF
    pdf = HTML(string=html_string).write_pdf()

    # Crea la respuesta HTTP con el PDF
    response = HttpResponse(pdf, content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="clientes_por_ruta_{ruta.id}.pdf"'

    return response
    