from django.shortcuts import render, redirect

from lodgings.models import Lodging

from .forms import LodgingForm

from django.http import JsonResponse

from django.contrib import messages

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

def detail_lodging(request, lodging_id):
    lodging = Lodging.objects.get(pk=lodging_id)
    data = { 'name': lodging.name, 'price': lodging.price, 'description': lodging.description}
    return JsonResponse(data)

def delete_lodging(request, lodging_id):
    lodging = Lodging.objects.get(pk=lodging_id)
    try:
        lodging.delete()        
        messages.success(request, 'Cabaña eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar la cabaña porque está asociado a una reserva.')
    return redirect('lodgings')


def edit_lodging(request, lodging_id):
    lodging = Lodging.objects.get(pk=lodging_id)
    form = LodgingForm(request.POST or None, request.FILES or None, instance=lodging)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'cabaña actualizada correctamente.')
        except:
            messages.error(request, 'Ocurrió un error al editar la  cabaña.')
        return redirect('lodgings')    
    return render(request, 'lodgings/editar.html', {'form': form})