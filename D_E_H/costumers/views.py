from django.shortcuts import render, redirect

from costumers.models import Costumer

def costumers(request):    
    costumers_list = Costumer.objects.all()    
    return render(request, 'costumers/index.html', {'costumers_list': costumers_list})

def change_status_costumers(request, costumer_id):
    costumer = Costumer.objects.get(pk=costumer_id)
    costumer.status = not costumer.status
    costumer.save()
    return redirect('costumers')