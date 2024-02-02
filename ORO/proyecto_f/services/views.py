from django.shortcuts import render, redirect

from services.models import Service

from .forms import ServiceForm

from django.http import JsonResponse

from django.contrib import messages


def create_service(request):
    form = ServiceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('services')    
    return render(request, 'services/create.html', {'form': form})

def services(request):    
    services_list = Service.objects.all()    
    return render(request, 'services/index.html', {'services_list': services_list})

def change_status_service(request, service_id):
    service = Service.objects.get(pk=service_id)
    service.status = not service.status
    service.save()
    return redirect('services')

def detail_service(request, service_id):
    service = Service.objects.get(pk=service_id)
    data = { 'name': service.name, 'price': service.price, 'description': service.description }    
    return JsonResponse(data)

def delete_service(request, service_id):
    service = Service.objects.get(pk=service_id)
    try:
        service.delete()        
        messages.success(request, 'Servicio eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar el Servicio porque está asociado a una reserva.')
    return redirect('services')