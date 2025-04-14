# bookings/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('create/<int:accommodation_id>/', views.booking_create, name='booking_create'),
    path('confirm/<int:pk>/', views.booking_confirm, name='booking_confirm'),
    path('dashboard/', views.booking_dashboard, name='booking_dashboard'),
]
