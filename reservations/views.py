from django.core.mail import send_mail
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic.edit import FormView
from django.views.generic import TemplateView
from .forms import BookingForm  # Import your BookingForm
from .models import Reservation, Customer


class Confirmed(TemplateView):
    template_name = 'reservations/success.html'


class Bookings(LoginRequiredMixin, FormView):
    template_name = 'reservations/reservation.html'  # Update with your template
    form_class = BookingForm
    success_url = 'confirmed'  # Update with your success URL

    def get(self, request, *args, **kwargs):
        template_name = "reservations/reservation.html"
        booking_form = BookingForm()  # Create an instance of the form
        return render(request, template_name, {'booking_form': booking_form})

    def form_valid(self, form):
        # ...
        reserved_table = form.cleaned_data['reserved_table']
        reserved_date = form.cleaned_data['reserved_date']
        reserved_time_slot = form.cleaned_data['reserved_time_slot']
        customer_count = form.cleaned_data['customer_count']
        customer_name = form.cleaned_data['customer_name']
        email = form.cleaned_data['email']
        phone_number = form.cleaned_data['phone_number']

        if reserved_table.reserved:
            # Table is already reserved
            return render(self.request, self.template_name, {'booking_form': form, 'message': 'Table already reserved'})

        # Check for any conflicting reservations
        conflicting_reservations = Reservation.objects.filter(
            reserved_table=reserved_table,
            reserved_date=reserved_date,
            reserved_time_slot=reserved_time_slot,
        )

        if conflicting_reservations.exists():
            # There are conflicting reservations
            return render(self.request, self.template_name, {'booking_form': form, 'message': 'Table conflicts with existing reservation'})

        # Mark the table as reserved
        reserved_table.reserved = True
        reserved_table.save()

        # Create a new reservation
        reservation = Reservation(
            customer_count=customer_count,
            reserved_date=reserved_date,
            reserved_time_slot=reserved_time_slot,
            reserved_table=reserved_table,
            customer=customer
        )

        # Save the reservation to the database
        reservation.save()

        return render(self.request, 'reservations/success.html')