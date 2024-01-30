from django.shortcuts import render, redirect

from payments.models import Payment

from .forms import PaymentForm

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