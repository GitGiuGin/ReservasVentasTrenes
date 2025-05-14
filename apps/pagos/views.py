from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from apps.reservas.models import Reserva
from apps.pagos.models import Pago

# Create your views here.
def registrar_pago(request, reserva_id):
    if request.method == 'POST':
        reserva = get_object_or_404(Reserva, id=reserva_id, cliente=request.user)
        total_a_pagar = request.POST.get('total_a_pagar')
        
        if hasattr(reserva, 'pago'):
            messages.error(request, 'El pago para esta reserva ya ha sido registrado.')
            return redirect('mi_cuenta')

        comprobante = request.FILES.get('pdf_documento')

        if comprobante:
            pago = Pago.objects.create(
                reserva=reserva,
                monto_total=total_a_pagar,
                comprobante=comprobante
            )
            reserva.estado = 'Pagado'
            reserva.save()
            messages.success(request, 'El pago ha sido registrado exitosamente.')
        else:
            messages.error(request, 'Por favor, complete todos los campos.')

    return redirect('mi_cuenta')