from django.shortcuts import render, redirect

from services.models import Service

def services(request):    
    services_list = Service.objects.all()    
    return render(request, 'services/index.html', {'services_list': services_list})

def change_status_service(request, service_id):
    service = Service.objects.get(pk=service_id)
    service.status = not service.status
    service.save()
    return redirect('services')