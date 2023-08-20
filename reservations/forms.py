from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField
from .models import Reservation, Customer

class BookingForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
        self.fields['reserved_date'].widget = forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()})

    # Include fields from both Reservation and Customer models
    customer_name = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Full name'}))
    email = forms.EmailField(
        widget=forms.EmailInput(attrs={'placeholder': 'Email address'}))
    phone_number = PhoneNumberField(
        widget=forms.TextInput(attrs={'placeholder': ('+353')}))

    class Meta:
        model = Reservation
        fields = ('customer_count', 'reserved_date', 'reserved_time_slot', 'customer_name', 'email', 'phone_number')
