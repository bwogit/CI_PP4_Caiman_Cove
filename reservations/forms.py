from .models import Booking
from django import forms


class BookingForm(forms.ModelForm):
    requested_date = forms.DateField()

    class Meta:
        model = Reservation
        fields = ('customer_capacity', 'reserved_date', 'reserved_time_slot')