from django.shortcuts import render, redirect

from rlodgings.models import Rlodging

from .forms import RlodgingForm

def create_rlodging(request):
    form = RlodgingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('rlodgings')    
    return render(request, 'rlodgings/create.html', {'form': form})

def rlodgings(request):    
    rlodgings_list = Rlodging.objects.all()    
    return render(request, 'lodgings/index.html', {'rlodgings_list': rlodgings_list})
