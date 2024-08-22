from django.shortcuts import render

# Create your views here:
def index(request):
    return render(request, 'clientes/clientes_index.html')  # Renderiza una plantilla llamada 'index.html'
