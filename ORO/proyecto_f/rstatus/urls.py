from . import views
from django.urls import path

urlpatterns = [      
    path('', views.rstatus, name='rstatus'),
	path('rstatu_status_/<int:rstatu_id>/', views.change_status_rstatu, name='rstatu_status'),  
]