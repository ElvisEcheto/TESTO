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
from decimal import Decimal


def create_reservation(request):
    costumers_list = Costumer.objects.all()
    lodgings_list = Lodging.objects.all()
    services_list = Service.objects.all()

    # Calcula days_difference aquí
    datess = request.POST.get('datess')  # Obtén la fecha de inicio desde la solicitud
    dateff = request.POST.get('dateff')  # Obtén la fecha final desde la solicitud

    # Realiza la validación y cálculo de days_difference aquí
    if datess and dateff:
        datess_date = datetime.strptime(datess, '%Y-%m-%d').date()
        dateff_date = datetime.strptime(dateff, '%Y-%m-%d').date()
        days_difference = (dateff_date - datess_date).days
    else:
        days_difference = 0  # Define un valor por defecto si las fechas no están presentes   
    
    if request.method == 'POST':
        # Obtener el correo electrónico del cliente del formulario
        costumer_email = request.POST['costumer']
        # Intentar obtener el objeto Costumer correspondiente al correo electrónico
        try:
            costumer = Costumer.objects.get(email=costumer_email)
        except Costumer.DoesNotExist:
            # Manejar la situación en la que no se encuentra un Costumer
            costumer = None  # Asignar None para manejarlo en la lógica de creación de la reserva
        
        datess_str = request.POST['datess']
        dateff_str = request.POST['dateff']        
        datess = datetime.strptime(datess_str, '%Y-%m-%d')
        dateff = datetime.strptime(dateff_str, '%Y-%m-%d')

        # Calcular los días de diferencia entre las fechas
        days_difference = (dateff - datess).days

        # Convertir el valor del campo totalValue a tipo Decimal
        total_value_str = request.POST['totalValue']
        total_value = Decimal(total_value_str)

        reservation = Reservation.objects.create(                   
            daterr=datetime.now().date(),                            
            datess=datess,
            dateff=dateff,
            price=total_value,  # Utilizar el valor convertido a Decimal
            rstatu='Reservado',
            costumer=costumer  # Asignar el objeto Costumer o None si no se encontró
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
    return render(request, 'reservations/create.html', {'costumers_list': costumers_list, 'lodgings_list': lodgings_list, 'services_list': services_list, 'days_difference': days_difference})



def detail_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    rlodgings = Rlodging.objects.filter(reservation=reservation)
    rservices = Rservice.objects.filter(reservation=reservation)
    payments = Payment.objects.filter(reservation=reservation)
    return render(request, 'reservations/detail.html', {'reservation': reservation, 'rlodgings': rlodgings, 'rservices': rservices, 'payments': payments})

def reservations(request):    
    reservations_list = Reservation.objects.all()    
    return render(request, 'reservations/index.html', {'reservations_list': reservations_list})


from django.core.exceptions import ObjectDoesNotExist

def edit_reservation(request, reservation_id):
    reservation = Reservation.objects.get(pk=reservation_id)
    rlodgings = Rlodging.objects.filter(reservation=reservation)
    rservices = Rservice.objects.filter(reservation=reservation)
    
    costumers_list = Costumer.objects.all()
    lodgings_list = Lodging.objects.all()
    services_list = Service.objects.all()

    total = 0  # Inicializamos la variable total
    total_with_days = 0  # Inicializamos el total con los días multiplicados

    if request.method == 'POST':
        # Procesar el formulario
        datess_str = request.POST.get('datess')
        dateff_str = request.POST.get('dateff')
        datess = datetime.strptime(datess_str, '%Y-%m-%d')
        dateff = datetime.strptime(dateff_str, '%Y-%m-%d')

        # Calcular los días de diferencia entre las fechas
        days_difference = (dateff - datess).days

        # Actualizar la reserva con los nuevos valores
        reservation.datess = datess
        reservation.dateff = dateff
        reservation.rstatu = 'Reservado'

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
        total_with_days = total * days_difference
        reservation.price = total_with_days
        reservation.save()

        # Redireccionar y mostrar un mensaje de éxito
        messages.success(request, '¡La reserva se ha editado exitosamente!')
        return redirect('reservations')

    # Calcular el total para mostrar en la vista
    total = sum(rlodging.price for rlodging in rlodgings) + sum(rservice.price for rservice in rservices)
    total_with_days = total * (reservation.dateff - reservation.datess).days
    
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
        'total_with_days': total_with_days,  # Pasamos el total con los días multiplicados
    })





from django.shortcuts import redirect
from django.urls import reverse

def delete_booking_cabin(request, id):
    rlodging = Rlodging.objects.get(pk=id)
    reservation_id = rlodging.reservation_id
    rlodging.delete()
    # Redirigir a la página de edición después de eliminar el registro
    return redirect('edit_reservation', reservation_id=reservation_id)

def delete_service_cabin(request, id):
    rservice = Rservice.objects.get(pk=id)
    reservation_id = rservice.reservation_id
    rservice.delete()
    # Redirigir a la página de edición después de eliminar el registro
    return redirect('edit_reservation', reservation_id=reservation_id)

from django.db.models import Sum

def index(request):
    reservations_list = Reservation.objects.all()
    return render(request, 'reservations/index.html', {'reservations_list': reservations_list})


def is_valid_price(price, field_type):
    try:
        return not math.isnan(float(price))
    except ValueError:
        return False




from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from .models import Reservation
from services.models import Service
from rservices.models import Rservice
from rlodgings.models import Rlodging
from payments.models import Payment
from io import BytesIO

def generate_pdf(request, reservation_id):
    # Obtener la reserva
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    

    # Obtener los servicios asociados a la reserva a través de la tabla de detalle
    reservation_services = Rservice.objects.filter(reservation=reservation)
    reservation_lodgings = Rlodging.objects.filter(reservation=reservation)
    reservation_payments = Payment.objects.filter(reservation=reservation)

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
        f"Estado: {reservation.costumer}",
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

    if reservation_lodgings:
        elements.append(Paragraph("Cabañas:", styles['Heading2']))
        for reservation_lodging in reservation_lodgings:
            lodging_detail = f"- {reservation_lodging.lodging.name}: ${reservation_lodging.price}"
            elements.append(Paragraph(lodging_detail, styles['Normal']))
            elements.append(Spacer(1, 3))


    if reservation_payments:
        elements.append(Paragraph("Pagos:", styles['Heading2']))
        for reservation_payment in reservation_payments:
            payment_detail = f"- {reservation_payment.date}: ${reservation_payment.value}"
            elements.append(Paragraph(payment_detail, styles['Normal']))
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

def cancelar_reserva(request, reservation_id):
    reserva = Reservation.objects.get(id=reservation_id)
    reserva.rstatu = 'Cancelado'
    reserva.save()
    return redirect('reservations')  # Redirige a la página que desees después de cancelar la reserva