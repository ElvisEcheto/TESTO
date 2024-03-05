from . import views
from django.urls import path
from django.urls import path
from .views import ReservationsPDFView

urlpatterns = [      
    path('', views.reservations, name='reservations'),
    path('create/', views.create_reservation, name='create_reservation'),
    path('detail/<int:reservation_id>/', views.detail_reservation, name='detail_reservation'),   
    path('edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'),
    path('reservas-pdf/', ReservationsPDFView.as_view(), name='reservas_pdf'),
]