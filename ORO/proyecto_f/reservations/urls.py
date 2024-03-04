from . import views
from django.urls import path

urlpatterns = [      
    path('', views.reservations, name='reservations'),
    path('create/', views.create_reservation, name='create_reservation'),
    path('detail/<int:reservation_id>/', views.detail_reservation, name='detail_reservation'),   
    path('edit/<int:reservation_id>/', views.edit_reservation, name='edit_reservation'), 
    path('ReservaP/<int:id>/', views.detail_pdf, name='ReservaP'),
]