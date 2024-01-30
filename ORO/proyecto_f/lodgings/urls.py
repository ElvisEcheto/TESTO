from . import views
from django.urls import path

urlpatterns = [      
    path('', views.lodgings, name='lodgings'),
	path('lodging_status_/<int:lodging_id>/', views.change_status_lodging, name='lodging_status'),
    path('create/', views.create_lodging, name='create_lodging'),          
]