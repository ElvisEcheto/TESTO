from django.shortcuts import render, redirect

from rservices.models import Rservice

from .forms import RserviceForm

def create_rservice(request):
    form = RserviceForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('rservices')    
    return render(request, 'rservices/create.html', {'form': form})

def rservices(request):    
    rservices_list = Rservice.objects.all()    
    return render(request, 'rservices/index.html', {'rservices_list': rservices_list})
