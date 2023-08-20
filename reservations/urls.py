# Imports

# 3rd party:
from django.urls import path

# Internal:
from reservations import views

urlpatterns = [
    path('reservations/', views.Bookings.as_view(), name='reservations'),
    path('confirmed/', views.Confirmed.as_view(), name='confirmed'),
]