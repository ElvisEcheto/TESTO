from . import views
from django.urls import path

urlpatterns = [      
    path('', views.clientes, name='clientes'),
    path('cliente_status_/<int:cliente_id>/', views.change_status_cliente, name='cliente_status'),
    ]