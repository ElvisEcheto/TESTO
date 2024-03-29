"""
URL configuration for proyecto_f project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path , include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Dashaboar/', views.index, name='index'),
    path('typedocuments/', include('typedocuments.urls')),
    path('rstatus/', include('rstatus.urls')),
    path('typelodgings/', include('typelodgings.urls')), 
    path('services/', include('services.urls')),   
    path('costumers/', include('costumers.urls')),  
    path('lodgings/', include('lodgings.urls')),  
    path('reservations/', include('reservations.urls')),  
    path('payments/', include('payments.urls')), 
    path('rservices/', include('rservices.urls')),
    path('rlodgings/', include('rlodgings.urls')),
    path('login',views.login, name='login'),
    path('logout',views.logout, name='logout'),
    path('',views.lading, name='lading'),
    path('Register',views.register, name='register'),
    path('Restore',views.recover_password, name='restore'),
    path('help/', views.help,name='help'),
]