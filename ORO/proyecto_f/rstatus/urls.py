from . import views
from django.urls import path

urlpatterns = [      
    path('', views.rstatus, name='rstatus'),
	path('rstatu_status_/<int:rstatu_id>/', views.change_status_rstatu, name='rstatu_status'),
    path('create/', views.create_rstatu, name='create_rstatu'),   
    path('detail/<int:rstatu_id>/', views.detail_rstatu, name='detail_rstatu'),
    path('delete/<int:rstatu_id>/', views.delete_rstatu, name='delete_rstatu'),
]