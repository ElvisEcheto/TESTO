from django.shortcuts import render, redirect

from reservations.models import Reservation

from .forms import ReservationForm

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
    rlodging = Rlodging.objects.filter(reservation=reservation)
    rservice = Rservice.objects.filter(reservation=reservation)

    costumers_list = Costumer.objects.all()
    lodgings_list = Lodging.objects.all()
    services_list = Service.objects.all()    
    
    if request.method == 'POST':
        datess_str = request.POST['datess']
        dateff_str = request.POST['dateff']        
        datess = datetime.strptime(datess_str, '%Y-%m-%d')
        dateff = datetime.strptime(dateff_str, '%Y-%m-%d')

        reservation.datess = datess
        reservation.dateff = dateff
        reservation.price = request.POST['totalValue']
        reservation.costumer_id = request.POST['costumer']
   
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
        messages.success(request, 'Reserva editada con éxito.')
        return redirect('reservations')
    return render(request, 'reservations/edit.html', {'reservation': reservation, 'costumers_list': costumers_list, 'lodgings_list': lodgings_list, 'services_list': services_list, 'rlodgings':rlodging, 'rservices':rservice })

from django.shortcuts import render
from django.http import HttpResponse
from wkhtmltopdf.views import PDFTemplateResponse

def detail_pdf(request, id):
    # Obtiene la reserva específica o muestra un error 404 si no existe
    reservation = Reservation.objects.get(id=id)

    # Lógica para obtener los datos necesarios para el template
    # Por ejemplo, puedes obtener `rlodgings`, `rservices`, `payments` de alguna forma

    context = {}

    # Renderiza el template y retorna una respuesta PDF
    return PDFTemplateResponse(request=request,template='reservations/detail.html', filename=f'detalle_reserva_{reservation.id}.pdf',context=context)