#imports
# -------------------------------------------------------------
# 3rd party:
from django.shortcuts import render
from django.views import generic

# -------------------------------------------------------------
# Internal:
from .models import Table, Customer, Reservation
# -------------------------------------------------------------
def bookings(request):
    """
    A view to display the booking list
    """
    booking_list = Reservation.objects.all()
    return render(
        request, 'reservations/reservation.html', {'booking_list': booking_list})