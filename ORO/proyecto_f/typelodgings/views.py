from django.shortcuts import render, redirect
from django.contrib import messages
from typelodgings.models import Typelodging
from django.http import JsonResponse
from .forms import TypelodgingForm


def create_typelodging(request):
    form = TypelodgingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('typelodgings')
    return render(request, 'typelodgings/create.html', {'form': form})

def typelodgings(request):
    typelodgings_list = Typelodging.objects.all()
    return render(request, 'typelodgings/index.html', {'typelodgings_list': typelodgings_list})

def change_status_typelodging(request, typelodging_id):
    typelodging = Typelodging.objects.get(pk=typelodging_id)
    typelodging.status = not typelodging.status
    typelodging.save()
    return redirect('typelodgings')


def detail_typelodging(request, typelodging_id):
    typelodging = Typelodging.objects.get(pk=typelodging_id)
    data = { 'name': typelodging.name}
    return JsonResponse(data)

def delete_typelodging(request, typelodging_id):
    typelodging = Typelodging.objects.get(pk=typelodging_id)
    try:
        typelodging.delete()        
        messages.success(request, 'Tipo cabaña eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar el tipo cabaña porque está asociado a una cabaña.')
    return redirect('typelodgings')