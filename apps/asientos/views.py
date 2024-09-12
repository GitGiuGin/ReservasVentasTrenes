from django.shortcuts import render

# Create your views here.
def liberarAsiento():
    pass

def obtenerEstado():
    pass

def reservasAsiento(request):
    # Aquí colocas la lógica para manejar la selección de asientos
    return render(request, 'asientos/seleccion_asiento.html')

def verificarDisponibilidad():
    pass