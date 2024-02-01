from . import views
from django.urls import path

urlpatterns = [      
    path('', views.costumers, name='costumers'),
	path('costumer_status_/<int:costumer_id>/', views.change_status_costumer, name='costumer_status'),
    path('create/', views.create_costumer, name='create_costumer'),   
    path('detail/<int:costumer_id>/', views.detail_costumer, name='detail_costumer'),   
    path('delete/<int:costumer_id>/', views.delete_costumer, name='delete_costumer'), 
]