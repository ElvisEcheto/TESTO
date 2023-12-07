from . import views
from django.urls import path

urlpatterns = [      
    path('', views.services, name='services'),  
    path('service_status_/<int:service_id>/', views.change_status_service, name='service_status'),          
]