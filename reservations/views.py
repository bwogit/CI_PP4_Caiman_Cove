
# from django.shortcuts import render, reverse, get_object_or_404
# from django.views import generic
# from django.views import View
# from django.http import HttpResponseRedirect
# from django.contrib.auth.models import User

# from .models import Table, Customer, Reservation
# from .forms import ReservationForm, CustomerForm
# # -------------------------------------------------------------

# def bookings(request):
#     """
#     A view to display the booking list
#     """
#     booking_list = Reservation.objects.all()
#     context = {'reservation_form': ReservationForm(), 'customer_form': CustomerForm()}
    
#     return render(
#         request, 'reservations/reservation.html', {'reservation_form': ReservationForm(), 'customer_form': CustomerForm()})
from django.shortcuts import render
from django.views import View
from .models import Table, Customer, Reservation
from .forms import ReservationForm, CustomerForm

class Bookings(View):
    """ Reservation view for guests to make bookings """

    def get(self, request, *args, **kwargs):
        template_name = "reservations/reservation.html"
        return render(request, template_name,
                      {'customer_form': CustomerForm(),
                       'reservation_form': ReservationForm()})

    def post(self, request, *args, **kwargs):
        customer_form = CustomerForm(data=request.POST)
        reservation_form = ReservationForm(request.POST)

        if reservation_form.is_valid() and customer_form.is_valid():
            reserved_date = request.POST.get('reserved_date')
            reserved_time = request.POST.get('reserved_time')
            customer_count = request.POST.get('customer_count')
            # Handle the valid form data here
            # You can access guest_form.cleaned_data and booking_form.cleaned_data
        else:
            booking_form = BookingForm()

        return render(request, "reservations/reservation.html",
                      {'customer_form': CustomerForm(),
                       'reservation_form': ReservationForm()})
