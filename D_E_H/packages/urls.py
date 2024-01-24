from . import views
from django.urls import path

urlpatterns = [      
    path('', views.packages, name='packages'),   
    path('package_status_/<int:packages_id>/', views.change_status_package, name='package_status'),   
    path('create/', views.create_package, name='create_package'),       
]