#imports
# -------------------------------------------------------------
# 3rd party:
from django.shortcuts import render, reverse, get_object_or_404
from django.views import generic
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

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