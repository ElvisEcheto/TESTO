from django.shortcuts import render, redirect

from reservations.models import Reservation

from .forms import ReservationForm

def create_reservation(request):
    form = ReservationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('reservations')    
    return render(request, 'reservations/create.html', {'form': form})

def reservations(request):    
    reservations_list = Reservation.objects.all()    
    return render(request, 'reservations/index.html', {'reservations_list': reservations_list})