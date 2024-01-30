from . import views
from django.urls import path

urlpatterns = [      
    path('', views.typedocuments, name='typedocuments'),
	path('typedocument_status_/<int:typedocument_id>/', views.change_status_typedocument, name='typedocument_status'),
    path('create/', views.create_typedocument, name='create_typedocument'),        
    path('detail/<int:typedocument_id>/', views.detail_typedocument, name='detail_typedocument'),  
    path('delete/<int:typedocument_id>/', views.delete_typedocument, name='delete_typedocument'),
]