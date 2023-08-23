# Imports

# 3rd party:
from django.urls import path

# Internal:
from reservations import views
from .views import BookingList

urlpatterns = [
    path('reservations/', views.Bookings.as_view(), name='reservations'),
    path('confirmed/', views.Confirmed.as_view(), name='confirmed'),
    path('bookings/', BookingList.as_view(), name='booking_list'),
    path('edit_booking/<int:pk>/', views.EditBooking.as_view(), name='edit_booking'),
    path('delete_booking/<int:pk>/', views.DeleteBooking.as_view(), name='delete_booking'),
]