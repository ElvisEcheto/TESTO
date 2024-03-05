from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.models import User
from proyecto_f.form import RegisterForm
from costumers.models import Costumer
from django.contrib.auth.models import Group
from django.db import models
from payments.models import Payment
from reservations.models import Reservation 
from lodgings.models import Lodging
from costumers.models import Costumer
from payments.models import Payment

def index(request):
    total_payments = Payment.objects.all().aggregate(total=models.Sum('value'))['total'] or 0
    total_reservations = Reservation.objects.count()
    costumers = Costumer.objects.all().count()
    lodgings = Lodging.objects.all()
    reservations = Reservation.objects.all().order_by('-price')
    payments = Payment.objects.all().order_by('-value')
    context = {'total_payments': total_payments, 
               'total_reservations': total_reservations ,
               'costumers' : costumers , 'lodgings' : lodgings , 'payments' : payments, 'reservations' : reservations }
    return render(request, 'index.html', context)

def login(request):
    error = None
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        authenticated_user = authenticate(username=username, password=password)
        if authenticated_user is not None:
            auth_login(request, authenticated_user)
            return render(request, 'index.html', {'user': authenticated_user})
        else:
            error = 'Usuario o contraseña incorrectos.'
            return render(request, 'login.html', {'error': error})    
        
    return render(request, 'login.html')

def logout(request):
    auth_logout(request)    
    return redirect('login')

def lading(request):
    return render(request,'lading.html')

def register(request):
    form = RegisterForm()
    if request.method == 'POST':
        form = RegisterForm(request.POST or None)
        if form.is_valid():
            name = form.cleaned_data['name']
            last_name = form.cleaned_data['last_name']
            document = form.cleaned_data['document']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            phone = form.cleaned_data['phone']
            username = email
            user = User.objects.create_user(username, email, password, first_name=name, last_name=last_name)
            user.save()
            group = Group.objects.get(name='clientes')
            user.groups.add(group)
            if user is not None:            
                costumer = Costumer.objects.filter(document=document).first()
                if costumer is None:
                    name = form.cleaned_data['name'] + ' ' + form.cleaned_data['last_name']
                    costumer = Costumer(None, name, document=document, email=email, phone=phone)
                    costumer.save()
                    return redirect('login')               
            return redirect('login')    
    return render(request, 'register.html', {'form': form})