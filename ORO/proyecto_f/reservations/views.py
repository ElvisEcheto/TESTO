from django.shortcuts import render, redirect

from reservations.models import Reservation

from .forms import ReservationForm

from django.http import JsonResponse

from django.contrib import messages


def create_reservation(request):
    form = ReservationForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('reservations')    
    return render(request, 'reservations/create.html', {'form': form})

def reservations(request):    
    reservations_list = Reservation.objects.all()    
    return render(request, 'reservations/index.html', {'reservations_list': reservations_list})

def detail_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    data = { 'coder': reservation.coder, 'daterr': reservation.daterr, 'value': reservation.value }    
    return JsonResponse(data)

def delete_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    try:
        reservation.delete()        
        messages.success(request, 'Reserva eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar la reserva porque está asociado a un pago.')
    return redirect('reservations')