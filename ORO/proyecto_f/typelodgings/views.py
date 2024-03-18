from django.shortcuts import render, redirect
from django.contrib import messages
from typelodgings.models import Typelodging
from django.http import JsonResponse
from .forms import TypelodgingForm

from django.contrib.auth.decorators import login_required


@login_required
def create_typelodging(request):
    if not request.user.is_superuser:
        return redirect('lodgings') 
    form = TypelodgingForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('typelodgings')
    return render(request, 'typelodgings/create.html', {'form': form})

@login_required
def typelodgings(request):
    if not request.user.is_superuser:
        return redirect('lodgings') 
    typelodgings_list = Typelodging.objects.all()
    return render(request, 'typelodgings/index.html', {'typelodgings_list': typelodgings_list})

@login_required
def change_status_typelodging(request, typelodging_id):
    if not request.user.is_superuser:
        return redirect('lodgings')
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

@login_required
def edit_typelodging(request, typelodging_id):
    if not request.user.is_superuser:
        return redirect('lodgings')
    typelodging = Typelodging.objects.get(pk=typelodging_id)
    form = TypelodgingForm(request.POST or None, instance=typelodging)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'tipo de cabaña actualizado correctamente.')
        except:
            messages.error(request, 'Ocurrió un error al editar el autor.')        
        return redirect('typelodgings')    
    return render(request, 'typelodgings/editar.html', {'form': form})