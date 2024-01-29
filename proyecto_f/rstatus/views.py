from django.shortcuts import render, redirect

from rstatus.models import Rstatu

from .forms import RstatuForm

def create_rstatu(request):
    form = RstatuForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('rstatus')    
    return render(request, 'rstatus/create.html', {'form': form})

def rstatus(request):    
    rstatus_list = Rstatu.objects.all()    
    return render(request, 'rstatus/index.html', {'rstatus_list': rstatus_list})

def change_status_rstatu(request, rstatu_id):
    rstatu = Rstatu.objects.get(pk=rstatu_id)
    rstatu.status = not rstatu.status
    rstatu.save()
    return redirect('rstatus')