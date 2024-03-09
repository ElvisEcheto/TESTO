from io import BytesIO
from django.shortcuts import render, redirect
from reservations.models import Reservation
from .forms import ReservationForm
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.contrib import messages
from datetime import datetime
from costumers.models import Costumer
from lodgings.models import Lodging
from services.models import Service
from reservations.models import Reservation
from rlodgings.models import Rlodging
from rservices.models import Rservice
from payments.models import Payment
from django.db.models import Sum, F, FloatField
from django.db.models.functions import Coalesce
from decimal import Decimal
import math




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

def reservations(request):    
    reservations_list = Reservation.objects.all()    
    return render(request, 'reservations/index.html', {'reservations_list': reservations_list})


def edit_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    rlodgings = Rlodging.objects.filter(reservation=reservation)
    rservices = Rservice.objects.filter(reservation=reservation)
    
    costumers_list = Costumer.objects.all()
    lodgings_list = Lodging.objects.all()
    services_list = Service.objects.all()

    total = 0  # Inicializamos la variable total

    if request.method == 'POST':
        # Procesar el formulario
        datess_str = request.POST.get('datess')
        dateff_str = request.POST.get('dateff')
        datess = datetime.strptime(datess_str, '%Y-%m-%d')
        dateff = datetime.strptime(dateff_str, '%Y-%m-%d')

        # Actualizar la reserva con los nuevos valores
        reservation.datess = datess
        reservation.dateff = dateff
        reservation.rstatu = 'Reservado'
        reservation.costumer_id = request.POST.get('costumer')
        
        # Guardar las nuevas cabañas y servicios seleccionados
        lodgings_Id = request.POST.getlist('lodgingId[]')
        lodgings_price = request.POST.getlist('lodgingPrice[]')
        services_Id = request.POST.getlist('serviceId[]')
        services_price = request.POST.getlist('servicePrice[]')

        # Guardar los nuevos registros
        for i in range(len(lodgings_Id)):
            try:
                lodging = Lodging.objects.get(pk=int(lodgings_Id[i]))
            except ObjectDoesNotExist:
                continue
            Rlodging.objects.create(
                reservation=reservation,
                lodging=lodging,
                price=float(lodgings_price[i])
            )

        for i in range(len(services_Id)):
            try:
                service = Service.objects.get(pk=int(services_Id[i]))
            except ObjectDoesNotExist:
                continue
            Rservice.objects.create(
                reservation=reservation,
                service=service,
                price=float(services_price[i])
            )

        # Calcular el total y asignarlo a la reserva
        total = sum(float(price) for price in lodgings_price + services_price)
        reservation.price = total
        reservation.save()

        messages.success(request, 'Reserva editada con éxito.')
        return redirect('reservations')

    # Calcular el total para mostrar en la vista
    total = sum(rlodging.price for rlodging in rlodgings) + sum(rservice.price for rservice in rservices)
    
    # Formatear el total para mostrar 0 en lugar de 0.00 cuando sea un número entero
    if total % 1 == 0:  # Verificar si el total es un número entero
        total = int(total)  # Convertir a entero si es necesario
    else:
        total = '{:.2f}'.format(total)  # De lo contrario, mantener dos decimales
    
    return render(request, 'reservations/edit.html', {
        'reservation': reservation,
        'costumers_list': costumers_list,
        'lodgings_list': lodgings_list,
        'services_list': services_list,
        'rlodgings': rlodgings,
        'rservices': rservices,
        'total': total,
    })



def delete_booking_cabin(request, id):
    rlodging = Rlodging.objects.get(pk=id)
    price = rlodging.price
    rlodging.delete()
    # Redirigir a la página de edición
    return redirect('edit_reservation', reservation_id=rlodging.reservation_id)

def delete_service_cabin(request, id):
    rservice = Rservice.objects.get(pk=id)
    price = rservice.price
    rservice.delete()
    # Redirigir a la página de edición
    return redirect('edit_reservation', reservation_id=rservice.reservation_id)

from django.db.models import Sum

def index(request):
    reservations_list = Reservation.objects.all()
    return render(request, 'reservations/index.html', {'reservations_list': reservations_list})


def is_valid_price(price, field_type):
    try:
        return not math.isnan(float(price))
    except ValueError:
        return False
