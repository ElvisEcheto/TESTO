from django.shortcuts import render, redirect

from payments.models import Payment

from django.http import JsonResponse

from .forms import PaymentForm

from django.contrib import messages






from django.shortcuts import render
from datetime import datetime
from django.shortcuts import redirect

from reservations.models import Reservation
from django.db import models
from . models import Payment


def payment_reservation(request, id):
    reservation = Reservation.objects.get(id=id)
    total_payments = Payment.objects.filter(reservation_id=id).aggregate(total=models.Sum('value'))
    if total_payments['total'] is not None:
        total_payments = total_payments['total']
    else:
        total_payments = 0    
    if request.method == 'POST':
        date = datetime.now().date()
        value = request.POST['value']
        methodpay = request.POST['methodpay']
        payment_reservation = request.POST['payment_reservation']
        payment = Payment.objects.create(
            date=date,
            value=int(value),
            methodpay=methodpay,
            reservation=reservation,
            status=1
        )
        try:
            payment.save()     
            total_p = Payment.objects.filter(reservation_id=id).aggregate(total=models.Sum('value'))       
            if  int(total_p['total']) >= (reservation.price / 2) and int(total_p['total']) < reservation.price:
                reservation.rstatu = 'Confirmada'
            elif int(total_p['total']) >= reservation.price:
                reservation.rstatu = 'En ejecución'        
            reservation.save()
            return redirect('reservations') 
        
        except Exception as e:
            return redirect('reservations')         
    return render(request, 'payment.html', {'reservation': reservation, 'total_payments': total_payments})







def create_payment(request):
    form = PaymentForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('payments')    
    return render(request, 'payments/create.html', {'form': form})

def payments(request):    
    payments_list = Payment.objects.all()    
    return render(request, 'payments/index.html', {'payments_list': payments_list})

def change_status_payment(request, payment_id):
    payment = Payment.objects.get(pk=payment_id)
    payment.status = not payment.status
    payment.save()
    return redirect('payments')

def detail_payment(request, payment_id):
    payment = Payment.objects.get(pk=payment_id)
    data = { 'date': payment.date, 'value': payment.value, 'methodpay': payment.methodpay }    
    return JsonResponse(data)

def delete_payment(request, payment_id):
    payment = Payment.objects.get(pk=payment_id)
    try:
        payment.delete()        
        messages.success(request, 'Pago eliminado correctamente.')
    except:
        messages.error(request, 'No se puede eliminar el pago porque está asociado a una tabla externa.')
    return redirect('payments')

def edit_payment(request, payment_id):
    payment = Payment.objects.get(pk=payment_id)
    form = PaymentForm(request.POST or None, request.FILES or None, instance=payment)
    if form.is_valid() and request.method == 'POST':
        try:
            form.save()
            messages.success(request, 'Libroactualizado correctamente.')
        except:
            messages.error(request, 'Ocurrió un error al editar el libro.')
        return redirect('payments')    
    return render(request, 'payments/edit.html', {'form': form})



