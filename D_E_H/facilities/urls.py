from . import views
from django.urls import path

urlpatterns = [      
    path('', views.facilities, name='facilities'),      
    path('facilitie_status_/<int:facilitie_id>/', views.change_status_facilitie, name='facilitie_status'),   
    path('create/', views.create_facilitie, name='create_facilitie'),                 
]