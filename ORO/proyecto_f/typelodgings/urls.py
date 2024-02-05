from . import views
from django.urls import path

urlpatterns = [
    path('', views.typelodgings, name='typelodgings'),
	path('typelodging_status_/<int:typelodging_id>/', views.change_status_typelodging, name='typelodging_status'),
    path('create/', views.create_typelodging, name='create_typelodging'),
    path('detail/<int:typelodging_id>/', views.detail_typelodging, name='detail_typelodging'),
    path('delete/<int:typelodging_id>/', views.delete_typelodging, name='delete_typelodging'),
    path('edit/<int:typelodging_id>/', views.edit_typelodging, name='edit_typelodging'),
]