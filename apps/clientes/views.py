from django.shortcuts import render

# Create your views here:
def index(request):
    return render(request, 'clientes/clientes_index.html')  # Renderiza una plantilla llamada 'index.html'

def clientesNew(request):
    return render(request, 'clientes/cliente_new.html')

def clientesEditar(request):
    return render(request, 'clientes/cliente_editar.html')

def clientesList(request):
    return render(request, 'clientes/cliente_list.html')