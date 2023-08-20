from django.shortcuts import render
from django.views import View
from .forms import BookingForm
from .models import Reservation, Customer

class Bookings(View):
    """ Reservation view for guests to make bookings """

    def get(self, request, *args, **kwargs):
        template_name = "reservations/reservation.html"
        booking_form = BookingForm()  # Create an instance of the combined form
        return render(request, template_name, {'booking_form': booking_form})

    def post(self, request, *args, **kwargs):
        booking_form = BookingForm(request.POST)

        if booking_form.is_valid():
            # Get the cleaned data from the form
            cleaned_data = booking_form.cleaned_data

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

            # Redirect the user to a success page or render a success message
            return render(request, "reservations/success.html")

        else:
            # If the form is not valid, re-render the template with the form and errors
            return render(request, "reservations/reservation.html", {'booking_form': booking_form})
