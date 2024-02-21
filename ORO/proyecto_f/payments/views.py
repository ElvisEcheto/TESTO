from django.shortcuts import render, redirect

from payments.models import Payment

from django.http import JsonResponse

from .forms import PaymentForm

from django.contrib import messages












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