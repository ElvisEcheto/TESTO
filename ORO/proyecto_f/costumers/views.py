from django.shortcuts import render, redirect

from costumers.models import Costumer

from django.http import JsonResponse

from django.contrib import messages

from .forms import CostumerForm

from django.contrib.auth.decorators import login_required


@login_required
def create_costumer(request):
    if not request.user.is_superuser:
        return redirect('costumers') 
    form = CostumerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        try:
            messages.success(request, 'Cliente creado correctamente.')
            form.save()
        except:
            messages.error(request, 'Ocurrió un error al crear un cliente.')         
        return redirect('costumers')    
    return render(request, 'costumers/create.html', {'form': form})
 
@login_required
def costumers(request):   
    if not request.user.is_superuser:
        return redirect('index')  
    costumers_list = Costumer.objects.all()    
    return render(request, 'costumers/index.html', {'costumers_list': costumers_list })

@login_required
def change_status_costumer(request, costumer_id):
    if not request.user.is_superuser:
        return redirect('costumers') 
    costumer = Costumer.objects.get(pk=costumer_id)
    costumer.status = not costumer.status
    costumer.save()
    return redirect('costumers')

def detail_costumer(request, costumer_id):
    costumer = Costumer.objects.get(pk=costumer_id)
    data = { 'name': costumer.name, 'document': costumer.document, 'email': costumer.email, 'phone' : costumer.phone,}    
    return JsonResponse(data)

@login_required
def delete_costumer(request, costumer_id):
    if not request.user.is_superuser:
        return redirect('costumers') 
    costumer = Costumer.objects.get(pk=costumer_id)
    try:
        costumer.delete()        
        messages.success(request, 'Cliente eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar el cliente porque está asociado a una Reserva.')
    return redirect('costumers')

@login_required
def edit_costumer(request, costumer_id):
    if not request.user.is_superuser:
        return redirect('costumers') 
    costumer = Costumer.objects.get(pk=costumer_id)
    form = CostumerForm(request.POST or None, request.FILES or None, instance=costumer)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'cliente actualizado correctamente.')
        except:
            messages.error(request, 'Ocurrió un error al editar el cliente.')
        return redirect('costumers')    
    return render(request, 'costumers/editar.html', {'form': form})