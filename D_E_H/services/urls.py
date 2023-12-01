from . import views
from django.urls import path

urlpatterns = [      
    path('', views.services, name='services'),  
    path('services_status_/<int:services_ID>/', views.change_status_services, name='service_status'),          
]