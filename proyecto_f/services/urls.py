from . import views
from django.urls import path

urlpatterns = [      
    path('', views.services, name='services'),
	path('services_status_/<int:services_id>/', views.change_status_service, name='service_status'),
    path('create/', views.create_service, name='create_service'),          
]