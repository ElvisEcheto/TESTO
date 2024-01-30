from django.shortcuts import render, redirect

from rstatus.models import Rstatu


def rstatus(request):    
    rstatus_list = Rstatu.objects.all()    
    return render(request, 'rstatus/index.html', {'rstatus_list': rstatus_list})

def change_status_rstatu(request, rstatu_id):
    rstatu = Rstatu.objects.get(pk=rstatu_id)
    rstatu.status = not rstatu.status
    rstatu.save()
    return redirect('rstatus')