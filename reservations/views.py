#imports
# -------------------------------------------------------------
# 3rd party:
from django.shortcuts import render
from django.views import generic

from .models import Table, Customer, Reservation
from .forms import ReservationForm, CustomerForm
# -------------------------------------------------------------
def bookings(request):
    """
    A view to display the booking list
    """
    booking_list = Reservation.objects.all()
    context = {'reservation_form': ReservationForm(), 'customer_form': CustomerForm()}
    return render(
        request, 'reservations/reservation.html', {'booking_list': booking_list})