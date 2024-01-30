from . import views
from django.urls import path

urlpatterns = [      
    path('', views.rlodgings, name='rlodgings'),
	path('rlodging_status_/<int:rlodging_id>/', views.change_status_rlodging, name='rlodging_status'),
    path('create/', views.create_rlodging, name='create_rlodging'),          
]