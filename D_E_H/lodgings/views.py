from django.shortcuts import render, redirect

from lodgings.models import Lodging

def lodgings(request):  
    lodgings_list = Lodging.objects.all()    
    return render(request, 'lodgings/index.html', {'lodging_list': lodgings_list})

def change_status_lodging(request, lodging_id):
    lodging = Lodging.objects.get(pk=lodging_id)
    lodging.status = not lodging.status
    lodging.save()
    return redirect('lodgings')