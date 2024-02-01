from django.shortcuts import render, redirect

from rstatus.models import Rstatu

from django.http import JsonResponse

from django.contrib import messages

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

def detail_rstatu(request, rstatu_id):
    rstatu = Rstatu.objects.get(pk=rstatu_id)
    data = { 'name': rstatu.name, 'description': rstatu.description }    
    return JsonResponse(data)

def delete_rstatu(request, rstatu_id):
    rstatu = Rstatu.objects.get(pk=rstatu_id)
    try:
        rstatu.delete()        
        messages.success(request, 'Estado de reserva eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar el autor porque está asociado a un libro.')
    return redirect('rstatus')