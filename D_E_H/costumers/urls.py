from . import views
from django.urls import path

urlpatterns = [      
    path('', views.costumers, name='costumers'),
    path('costumer_status_/<int:costumer_id>/', views.change_status_costumers, name='costumer_status'),      
]