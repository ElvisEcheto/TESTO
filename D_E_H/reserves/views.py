from django.shortcuts import render, redirect

from reserves.models import Reserve

def reserves(request):    
    reserves_list = Reserve.objects.all()    
    return render(request, 'reserves/index.html', {'reserve_list': reserves_list})

def change_status_reserve(request, reserve_id):
    reserve = Reserve.objects.get(pk=reserve_id)
    reserve.status = not reserve.status
    reserve.save()
    return redirect('reserves')
