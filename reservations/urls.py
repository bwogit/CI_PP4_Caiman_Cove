# Imports

# 3rd party:
from django.urls import path

# Internal:
from reservations import views

urlpatterns = [
    path('reservations/', views.bookings, name='reservations'),
]