from . import views
from django.urls import path

urlpatterns = [      
    path('', views.type_lodgings, name='type_lodgings'),     
    path('type_lodging_status_/<int:type_lodging_id>/', views.change_status_type_lodging, name='type_lodging_status'),                   
]