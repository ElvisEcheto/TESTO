from django.shortcuts import render, redirect

from type_lodgings.models import Type_Lodging

def type_lodgings(request):    
    type_lodgings_list = Type_Lodging.objects.all()    
    return render(request, 'type_lodgings/index.html', {'type_lodgings_list': type_lodgings_list})

def change_status_type_lodging(request, type_lodging_id):
    type_lodging = Type_Lodging.objects.get(pk=type_lodging_id)
    type_lodging.status = not type_lodging.status
    type_lodging.save()
    return redirect('type_lodgings')  