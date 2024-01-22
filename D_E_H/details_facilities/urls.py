from . import views
from django.urls import path

urlpatterns = [      
    path('', views.details_facilities, name='details_facilities'),
		path('details_facilitie_status_/<int:details_facilitie_id>/', views.change_status_details_facilitie, name='details_facilitie_status'),   
    path('create/', views.create_details_facilitie, name='create_details_facilitie'),           
]