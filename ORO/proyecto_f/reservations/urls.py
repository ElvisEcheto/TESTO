from . import views
from django.urls import path
from django.urls import path

urlpatterns = [      
    path('', views.reservations, name='reservations'),
    path('create/', views.create_reservation, name='create_reservation'),
    path('detail/<int:reservation_id>/', views.detail_reservation, name='detail_reservation'),   
    path('edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('delete_booking_cabin/<int:id>/', views.delete_booking_cabin, name='delete_booking_cabin'),
    path('delete_service_cabin/<int:id>/', views.delete_service_cabin, name='delete_service_cabin'),
    path('reservation/<int:reservation_id>/pdf/', views.generate_pdf, name='generate_pdf'),
    path('cancelar-reserva/<int:reservation_id>/', views.cancelar_reserva, name='cancelar_reserva'),
     path('generate-reporte/<int:reservation_id>/', views.generate_reporte, name='generate_reporte'),
    
]