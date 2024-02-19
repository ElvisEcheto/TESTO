from django.shortcuts import render, redirect

from reservations.models import Reservation

from .forms import ReservationForm

from django.contrib import messages

from datetime import datetime

from costumers.models import Costumer

from lodgings.models import Lodging

from services.models import Service

from rlodgings.models import Rlodging

from rservices.models import Rservice

from payments.models import Payment

def reservations(request):    
    reservations_list = Reservation.objects.all()    
    return render(request, 'reservations/index.html', {'reservations_list': reservations_list})

def create_reservation(request):
    costumers_list = Costumer.objects.all()
    lodgings_list = Lodging.objects.all()
    services_list = Service.objects.all()    
    
    if request.method == 'POST':
        datess_str = request.POST['datess']
        dateff_str = request.POST['dateff']        
        datess = datetime.strptime(datess_str, '%Y-%m-%d')
        dateff = datetime.strptime(dateff_str, '%Y-%m-%d')

        reservation = Reservation.objects.create(                        
            daterr=datetime.now().date(),                                   
            datess=datess,
            dateff=dateff,
            price=request.POST['totalValue'],
            rstatu='Reservado',
            costumer_id=request.POST['costumer']
        )
        reservation.save()        
        lodgings_Id = request.POST.getlist('lodgingId[]')
        lodgings_price = request.POST.getlist('lodgingPrice[]')
        services_Id = request.POST.getlist('serviceId[]')
        services_price = request.POST.getlist('servicePrice[]')       
                
        for i in range(len(lodgings_Id)):            
            lodging = Lodging.objects.get(pk=int(lodgings_Id[i]))
            rlodging = Rlodging.objects.create(
                reservation=reservation,
                lodging=lodging,
                price=lodgings_price[i]
            )
            rlodging.save()
        
        for i in range(len(services_Id)):
            service = Service.objects.get(pk=int(services_Id[i]))
            rservice = Rservice.objects.create(
                reservation=reservation,
                service=service,
                price=services_price[i]
            )
            rservice.save()              
        messages.success(request, 'Reserva creada con éxito.')
        return redirect('reservations')
    return render(request, 'reservations/create.html', {'costumers_list': costumers_list, 'lodgings_list': lodgings_list, 'services_list': services_list})

def detail_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    rlodgings = Rlodging.objects.filter(reservation=reservation)
    rservices = Rservice.objects.filter(reservation=reservation)
    payments = Payment.objects.filter(reservation=reservation)
    return render(request, 'reservations/detail.html', {'reservation': reservation, 'rlodgings': rlodgings, 'rservices': rservices, 'payments': payments})

def delete_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    try:
        reservation.delete()        
        messages.success(request, 'Reserva eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar la reserva porque está asociado a un pago.')
    return redirect('reservations')

def edit_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    form = ReservationForm(request.POST or None, request.FILES or None, instance=reservation)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Libroactualizado correctamente.')
        except:
            messages.error(request, 'Ocurrió un error al editar el libro.')
        return redirect('reservations')    
    return render(request, 'reservations/edit.html', {'form': form})

