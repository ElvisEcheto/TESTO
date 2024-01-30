from . import views
from django.urls import path

urlpatterns = [      
    path('', views.costumers, name='costumers'),
	path('costumer_status_/<int:costumer_id>/', views.change_status_costumer, name='costumer_status'),
    path('create/', views.create_costumer, name='create_costumer'),     
]