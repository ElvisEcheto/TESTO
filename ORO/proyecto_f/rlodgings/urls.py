from . import views
from django.urls import path

urlpatterns = [      
    path('', views.rlodgings, name='rlodgings'),
    path('create/', views.create_rlodging, name='create_rlodging'),          
]