from . import views
from django.urls import path

urlpatterns = [      
    path('', views.reserves, name='reserves'),
		path('reserve_status_/<int:reserve_id>/', views.change_status_reserve, name='reserve_status'),            
]