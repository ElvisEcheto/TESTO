from django.shortcuts import render, redirect

from type_lodgings.models import Type_Lodging

from .forms import Type_LodgingForm

def create_type_lodging(request):
    form = Type_LodgingForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('type_lodgings')    
    return render(request, 'type_Lodgings/create.html', {'form': form})

def type_lodgings(request):    
    type_lodgings_list = Type_Lodging.objects.all()    
    return render(request, 'type_lodgings/index.html', {'type_lodgings_list': type_lodgings_list})

def change_status_type_lodging(request, type_lodging_id):
    type_lodging = Type_Lodging.objects.get(pk=type_lodging_id)
    type_lodging.status = not type_lodging.status
    type_lodging.save()
    return redirect('type_lodgings')  