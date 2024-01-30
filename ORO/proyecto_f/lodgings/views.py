from django.shortcuts import render, redirect

from lodgings.models import Lodging

from .forms import LodgingForm

def create_lodging(request):
    form = LodgingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('lodgings')    
    return render(request, 'lodgings/create.html', {'form': form})

def lodgings(request):    
    lodgings_list = Lodging.objects.all()    
    return render(request, 'lodgings/index.html', {'lodgings_list': lodgings_list})

def change_status_lodging(request, lodging_id):
    lodging = Lodging.objects.get(pk=lodging_id)
    lodging.status = not lodging.status
    lodging.save()
    return redirect('lodgings')