from django.shortcuts import render, redirect

from costumers.models import Costumer

from django.http import JsonResponse

from django.contrib import messages

from .forms import CostumerForm

def create_costumer(request):
    form = CostumerForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('costumers')    
    return render(request, 'costumers/create.html', {'form': form})

def costumers(request):    
    costumers_list = Costumer.objects.all()    
    return render(request, 'costumers/index.html', {'costumers_list': costumers_list })

def change_status_costumer(request, costumer_id):
    costumer = Costumer.objects.get(pk=costumer_id)
    costumer.status = not costumer.status
    costumer.save()
    return redirect('costumers')

def detail_costumer(request, costumer_id):
    costumer = Costumer.objects.get(pk=costumer_id)
    data = { 'name': costumer.name, 'document': costumer.document, 'email': costumer.email, 'phone' : costumer.phone, 'typedocument': str(costumer.typedocument) }    
    return JsonResponse(data)

def delete_costumer(request, costumer_id):
    costumer = Costumer.objects.get(pk=costumer_id)
    try:
        costumer.delete()        
        messages.success(request, 'Cliente eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar el cliente porque está asociado a una Reserva.')
    return redirect('costumers')