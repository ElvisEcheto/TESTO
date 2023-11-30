from django.shortcuts import render, redirect

from services.models import Services

def services(request):    
    services_list = Services.objects.all()    
    return render(request, 'services/index.html', {'services_list': services_list})

def change_status_costumers(request, costumer_id):
    costumer = Costumer.objects.get(pk=costumer_id)
    costumer.status = not costumer.status
    costumer.save()
    return redirect('costumers')