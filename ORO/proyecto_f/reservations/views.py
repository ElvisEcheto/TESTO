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



from django.db.models.signals import post_save
from django.dispatch import receiver
from payments.models import Payment

@receiver(post_save, sender=Payment)
def actualizar_columna_texto(sender, instance, created, **kwargs):
    if instance.value > 10:
        texto = 'pagado'
    elif instance.value  >= 5:
        texto = 'confirmado'
    elif instance.value  <= 0:
        texto = 'cancelado'
    else:
        texto = 'reservado'  # Valor predeterminado
    
    Reservation.objects.filter(id=instance.reservation_id).update(rstatu=texto)





def create_reservation(request):
    costumers_list = Costumer.objects.all()
    lodgings_list = Lodging.objects.all()
    services_list = Service.objects.all()    
    
    if request.method == 'POST':
        coder_str = request.POST['coder']
        datess_str = request.POST['datess']
        dateff_str = request.POST['dateff']        
        datess = datetime.strptime(datess_str, '%Y-%m-%d')
        dateff = datetime.strptime(dateff_str, '%Y-%m-%d')
        coder = coder_str

        reservation = Reservation.objects.create(                   
            daterr=datetime.now().date(),
            coder=coder,                                
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
    costumers_list = Costumer.objects.all()
    lodgings_list = Lodging.objects.all()
    services_list = Service.objects.all()    
    
    if request.method == 'POST':
        coder_str = request.POST['coder']
        datess_str = request.POST['datess']
        dateff_str = request.POST['dateff']        
        datess = datetime.strptime(datess_str, '%Y-%m-%d')
        dateff = datetime.strptime(dateff_str, '%Y-%m-%d')
        coder = coder_str

        # Actualizar los campos del objeto reservation con los valores recibidos del formulario
        reservation.datess = datess
        reservation.dateff = dateff
        reservation.coder = coder
        reservation.price = request.POST['totalValue']
        reservation.costumer_id = request.POST['costumer']
        
        # Guardar los cambios en la base de datos
        reservation.save()        

        # Actualizar los objetos relacionales Rlodging y Rservice
        lodgings_Id = request.POST.getlist('lodgingId[]')
        lodgings_price = request.POST.getlist('lodgingPrice[]')
        services_Id = request.POST.getlist('serviceId[]')
        services_price = request.POST.getlist('servicePrice[]')       

        # Eliminar los objetos Rlodging y Rservice existentes asociados a esta reserva
        reservation.rlodging_set.all().delete()
        reservation.rservice_set.all().delete()

        # Crear nuevos objetos Rlodging y Rservice con los valores actualizados
        for i in range(len(lodgings_Id)):            
            lodging = Lodging.objects.get(pk=int(lodgings_Id[i]))
            rlodging = Rlodging.objects.create(
                reservation=reservation,
                lodging=lodging,
                price=lodgings_price[i]
            )
        
        for i in range(len(services_Id)):
            service = Service.objects.get(pk=int(services_Id[i]))
            rservice = Rservice.objects.create(
                reservation=reservation,
                service=service,
                price=services_price[i]
            )
              
        # Redireccionar a la página de listado de reservas con un mensaje de éxito
        messages.success(request, 'Reserva editada con éxito.')
        return redirect('reservations')
    
    # Si la solicitud es GET, renderizar el formulario de edición con los datos del objeto reservation
    return render(request, 'reservations/edit.html', {'reservation': reservation, 'costumers_list': costumers_list, 'lodgings_list': lodgings_list, 'services_list': services_list})