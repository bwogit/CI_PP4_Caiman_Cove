from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import BookingForm  # Import your BookingForm
from .models import Reservation, Customer


class Confirmed(TemplateView):
    template_name = 'reservations/confirmed.html'


class Bookings(LoginRequiredMixin, FormView):
    template_name = 'reservations/reservation.html'  # Update with your template
    form_class = BookingForm
    success_url = 'confirmed'  # Update with your success URL

    def get(self, request, *args, **kwargs):
        template_name = "reservations/reservation.html"
        booking_form = BookingForm()  # Create an instance of the form
        return render(request, template_name, {'booking_form': booking_form})

    def form_valid(self, form):
        # Handle the form submission here
        cleaned_data = form.cleaned_data
        # Extract data from the cleaned_data dictionary
        customer_count = cleaned_data['customer_count']
        reserved_date = cleaned_data['reserved_date']
        reserved_time_slot = cleaned_data['reserved_time_slot']
        customer_name = cleaned_data['customer_name']
        email = cleaned_data['email']
        phone_number = cleaned_data['phone_number']

        # Check if the customer already exists
        customer, created = Customer.objects.get_or_create(
            customer_name=customer_name,
            email=email,
            phone=phone_number
        )

        # Create a new reservation instance with the extracted data and customer
        reservation = Reservation(
            customer_count=customer_count,
            reserved_date=reserved_date,
            reserved_time_slot=reserved_time_slot,
            customer=customer
        )

        # Save the reservation to the database
        reservation.save()

        #return render(self.request, self.template_name, {'booking_form': form})
        return redirect('confirmed')