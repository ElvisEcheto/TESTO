from django.shortcuts import render, redirect

from clientes.models import Cliente
def clientes(request):
    return render(request, 'clientes/index.html')

def Clientes(request):    
    clientes_list = Cliente.objects.all() 
    print(clientes_list)  
    return render(request, 'clientes/index.html', {'clientes_list': clientes_list})

def change_status_cliente(request, cliente_id):
    cliente = Cliente.objects.get(pk=cliente_id)
    cliente.status = not cliente.status
    cliente.save()
    return redirect('clientes')

