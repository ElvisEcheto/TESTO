from django.shortcuts import render, redirect

from reserves.models import Reserve

from .forms import ReserveForm

def create_reserve(request):
    form = ReserveForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('reserves')    
    return render(request, 'reserves/create.html', {'form': form})

def reserves(request):    
    reserves_list = Reserve.objects.all()    
    return render(request, 'reserves/index.html', {'reserve_list': reserves_list})

def change_status_reserve(request, reserve_id):
    reserve = Reserve.objects.get(pk=reserve_id)
    reserve.status = not reserve.status
    reserve.save()
    return redirect('reserves')
