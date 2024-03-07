
from io import BytesIO
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



from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .models import Reservation
import datetime

def generate_pdf(request, reservation_id):
    # Obtener la reserva
    reservation = get_object_or_404(Reservation, pk=reservation_id)

    # Obtener los servicios asociados a la reserva a través de la tabla de detalle
    reservation_services = Rservice.objects.filter(reservation=reservation)

    # Crear un buffer de bytes para almacenar el PDF
    buffer = BytesIO()

    # Crear el documento PDF
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    # Crear una lista para contener los elementos del PDF
    elements = []

    # Agregar el título
    title = Paragraph("Reserva", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Agregar los detalles de la reserva como párrafos
    details = [
        f"Fecha de Entrada: {reservation.datess}",
        f"Fecha de Salida: {reservation.dateff}",
        f"Precio: {reservation.price}",
        f"Estado: {reservation.rstatu}",
    ]
    for detail in details:
        elements.append(Paragraph(detail, styles['Normal']))
        elements.append(Spacer(1, 6))

    # Agregar los servicios asociados a la reserva
    if reservation_services:
        elements.append(Paragraph("Servicios:", styles['Heading2']))
        for reservation_service in reservation_services:
            service_detail = f"- {reservation_service.service.name}: ${reservation_service.price}"
            elements.append(Paragraph(service_detail, styles['Normal']))
            elements.append(Spacer(1, 3))

    # Construir el PDF
    pdf.build(elements)

    # Obtener el contenido del buffer y crear la respuesta HTTP
    pdf_buffer = buffer.getvalue()
    buffer.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reservation_{reservation_id}.pdf"'
    response.write(pdf_buffer)
    return response
    # Obtener la reserva
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    services = reservation.Service_set.all()

    # Crear un buffer de bytes para almacenar el PDF
    buffer = BytesIO()

    # Crear el documento PDF
    pdf = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()

    # Crear una lista para contener los elementos del PDF
    elements = []

    # Agregar el título
    title = Paragraph("Reserva", styles['Title'])
    elements.append(title)
    elements.append(Spacer(1, 12))

    # Agregar los detalles de la reserva como párrafos
    details = [
        f"Fecha de Entrada: {reservation.datess}",
        f"Fecha de Salida: {reservation.dateff}",
        f"Precio: {reservation.price}",
        f"Estado: {reservation.rstatu}",
    ]
    for detail in details:
        elements.append(Paragraph(detail, styles['Normal']))
        elements.append(Spacer(1, 6))
    
    if services:
        elements.append(Paragraph("Servicios:", styles['Heading2']))
        for service in services:
            service_detail = f"- {service.name}: ${service.price}"
            elements.append(Paragraph(service_detail, styles['Normal']))
            elements.append(Spacer(1, 3))


    # Construir el PDF
    pdf.build(elements)

    # Obtener el contenido del buffer y crear la respuesta HTTP
    pdf_buffer = buffer.getvalue()
    buffer.close()
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="reservation_{reservation_id}.pdf"'
    response.write(pdf_buffer)
    return response