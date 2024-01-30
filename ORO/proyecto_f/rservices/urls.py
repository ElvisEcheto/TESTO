from . import views
from django.urls import path

urlpatterns = [      
    path('', views.rservices, name='rservices'),
    path('create/', views.create_rservice, name='create_rservice'),          
]