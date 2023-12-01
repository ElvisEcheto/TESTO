from django.shortcuts import render, redirect

from services.models import Services

def services(request):    
    services_list = Services.objects.all()    
    return render(request, 'services/index.html', {'services_list': services_list})

def change_status_services(request, service_ID):
    service = Services.objects.get(pk=service_ID)
    service.status = not service.status
    service.save()
    return redirect('services')