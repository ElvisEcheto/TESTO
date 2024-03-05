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
        reservation.rstatu = 'Reservado'
        reservation.costumer_id = request.POST['costumer']
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

        messages.success(request, 'Reserva editada con éxito.')
        return redirect('reservations')

    return render(request, 'reservations/edit.html', {'reservation': reservation, 'costumers_list': costumers_list, 'lodgings_list': lodgings_list, 'services_list': services_list, 'rlodgings': rlodging, 'rservices': rservice})

from django.http import HttpResponse
from django.views.generic import View
from reportlab.pdfgen import canvas
from .models import Reservation
from payments.models import Payment  # Importamos el modelo de pagos

class ReservationsPDFView(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="reservas.pdf"'

        # Creamos el documento PDF
        p = canvas.Canvas(response)

        # Obtenemos todas las reservas
        reservations = Reservation.objects.all()

        # Iteramos sobre cada reserva y escribimos sus datos en el PDF
        for reservation in reservations:
            # Obtener los datos relevantes de la reserva
            datos_reserva = [
                f"Nombre: {reservation.id}",
                f"Fecha de inicio: {reservation.datess}",
                f"Fecha de fin: {reservation.dateff}"
            ]

            # Escribir los datos de la reserva en el PDF
            y = self.escribir_datos_en_pdf(p, datos_reserva)

            # Obtener los pagos relacionados con esta reserva
            pagos = Payment.objects.filter(reservation=reservation)

            # Si hay pagos relacionados, agregar la información de los pagos al PDF
            if pagos.exists():
                datos_pagos = ["--- Pagos ---"]
                for pago in pagos:
                    datos_pago = f"Monto: {pago.value}, Fecha: {pago.date}"
                    datos_pagos.append(datos_pago)
                
                # Escribir los datos de los pagos en el PDF
                y = self.escribir_datos_en_pdf(p, datos_pagos, y)

            # Agregar un salto de página después de cada reserva
            p.showPage()

        p.save()

        return response

    def escribir_datos_en_pdf(self, p, datos, y=None):
        """
        Función para escribir datos en el PDF y actualizar la posición 'y'.
        """
        if y is None:
            y = 750  # Posición inicial en el eje Y

        for dato in datos:
            p.drawString(100, y, dato)
            y -= 20  # Espacio vertical entre cada dato
        
        return y