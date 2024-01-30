from . import views
from django.urls import path

urlpatterns = [      
    path('', views.rservices, name='rservices'),
	path('rservice_status_/<int:rservice_id>/', views.change_status_rservice, name='rservice_status'),
    path('create/', views.create_rservice, name='create_rservice'),          
]