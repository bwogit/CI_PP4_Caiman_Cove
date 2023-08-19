from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField
from .models import Reservation, Customer

class ReservationForm(forms.ModelForm):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))
        
        requested_date = forms.DateField()
        widget=forms.DateInput(
            attrs={'type': 'date', 'min': datetime.now().date()})


    class Meta:
        model = Reservation
        fields = ('customer_count', 'reserved_date', 'reserved_time_slot')


class CustomerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.add_input(Submit('submit', 'Submit'))

    phone_number = PhoneNumberField(widget=forms.TextInput(
        attrs={'placeholder': ('+353')}))

    class Meta:
        model = Customer
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Full name'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'Email address'}),
        }
        fields = ('customer_name', 'email', 'phone')
