from . import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [      
    path('', views.clientes, name='clientes'),
    path('clientes_status_/<int:clientes_id>/', views.change_status_clientes, name='clientes_status'), 
]