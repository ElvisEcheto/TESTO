from . import views
from django.urls import path

urlpatterns = [      
    path('', views.lodgings, name='lodgings'),
		path('lodging_status_/<int:lodging_id>/', views.change_status_lodging, name='lodging_status'),            
]