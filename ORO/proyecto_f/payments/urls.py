from . import views
from django.urls import path

urlpatterns = [      
    path('', views.payments, name='payments'),
	path('payment_status_/<int:payment_id>/', views.change_status_payment, name='payment_status'),
    path('create/', views.create_payment, name='create_payment'),          
]