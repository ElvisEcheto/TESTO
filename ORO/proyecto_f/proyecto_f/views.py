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
from services.models import Service
from django.contrib import messages

def recover_password(request):    
    if request.method == 'POST':
        email = request.POST.get('email', '')  # Obtener el email del formulario
        
        # Verificar si el email existe en la base de datos
        if User.objects.filter(email=email).exists():
            """ Cosultar el usuario por el correo  y cambiar la contraseña encriptada"""
            recuperar_contraseña(email)
            return redirect('login')
        else:
            messages.error(request, 'Inserte un correo existente.')
            return render(request, 'restore.html')
    
    return render(request, 'restore.html')


import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import random
import string

from django.shortcuts import render

def generar_contraseña():
    caracteres = string.ascii_letters + string.digits
    longitud = 10
    return ''.join(random.choice(caracteres) for i in range(longitud))

def enviar_correo(destinatario, contraseña):
    # Configuración del servidor SMTP
    smtp_server = 'smtp.gmail.com'
    puerto = 587
    remitente = 'glampingcelestial@gmail.com'
    contraseña_smtp = 'uoob mcva wojt adal'

    # Crear el mensaje
    mensaje = MIMEMultipart()
    mensaje['From'] = remitente
    mensaje['To'] = destinatario
    mensaje['Subject'] = 'Recuperación de contraseña'

    cuerpo = f'Tu nueva contraseña es: {contraseña}'
    mensaje.attach(MIMEText(cuerpo, 'plain' , 'utf-8'))

    # Iniciar sesión en el servidor SMTP
    servidor = smtplib.SMTP(smtp_server, puerto)
    servidor.starttls()
    servidor.login(remitente, contraseña_smtp)

    # Enviar el correo electrónico
    servidor.send_message(mensaje)

    # Cerrar la conexión
    servidor.quit()

# Función principal
def recuperar_contraseña(email):
    correo_destino = email
    nueva_contraseña = generar_contraseña()
    enviar_correo(correo_destino, nueva_contraseña)
    if cambiar_contraseña_usuario(correo_destino, nueva_contraseña):
        print("La contraseña del usuario ha sido cambiada exitosamente.")
    else:
        print("No se pudo cambiar la contraseña del usuario. El usuario no fue encontrado.")

from django.contrib.auth.models import User

def cambiar_contraseña_usuario(email, nueva_contraseña):
    try:
        usuario = User.objects.get(email=email)
        usuario.set_password(nueva_contraseña)
        usuario.save()
        return True  # Indica que la contraseña fue cambiada exitosamente
    except User.DoesNotExist:
        return False  # Indica que no se encontró ningún usuario con el correo electrónico especificado

def dasboard(request):
    lodgings = Lodging.objects.all()
    return render(request,'lading.html')

def index(request):
    usuario = request.user
    total_payments = Payment.objects.all().aggregate(total=models.Sum('value'))['total'] or 0
    total_reservations = Reservation.objects.count()
    costumers = Costumer.objects.all().count()
    lodgings = Lodging.objects.all()
    services = Service.objects.all()
    reservations = Reservation.objects.all().order_by('-price')[:5]
    payments = Payment.objects.all().order_by('-value')[:5]
    context = {'usuario': usuario, 
               'total_payments': total_payments, 
               'total_reservations': total_reservations ,
               'costumers' : costumers , 
               'lodgings' : lodgings ,
               'services' : services,
               'reservations' : reservations, 
               'payments' : payments, }
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
    lodgings = Lodging.objects.all()
    
    return render(request, 'lading.html', {'lodgings': lodgings})

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

def help (request):
    return render(request, 'help.html')