# Imports
# 3rd party:
from crispy_forms.helper import FormHelper
from phonenumber_field.formfields import PhoneNumberField
# Internal
from datetime import datetime
from .models import Reservation
from django import forms


def validate_phone_number(value):
    phone_number = to_python(value)
    if phone_number and not phone_number.is_valid():
        raise ValidationError('Invalid phone number.')


class BookingForm(forms.ModelForm):
    """
    A form to gather booking information from users.
    It is based on the Reservation model and provides validation.
    """
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    reserved_date = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date', 'min':
                               datetime.now().date()}))

    phone = PhoneNumberField(widget=forms.TextInput(
        attrs={'placeholder': ('+569123456789')}))

    class Meta:
        model = Reservation
        fields = (
            'name',
            'phone',
            'email',
            'guest_count',
            'table',
            'reserved_date',
            'reserved_time_slot',
        )
