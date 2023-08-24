from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField
from .models import Reservation, Table
from .models import status_options


class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    reserved_date = forms.DateField(
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()}))

    phone = PhoneNumberField(widget=forms.TextInput(
        attrs={'placeholder': ('+353123456789')}))

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