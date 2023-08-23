from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from datetime import datetime
from phonenumber_field.formfields import PhoneNumberField
from .models import Reservation, Table
from .models import status_options

# class BookingForm(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.helper = FormHelper(self)
#         self.helper.add_input(Submit('submit', 'Submit'))
#         self.fields['reserved_date'].widget = forms.DateInput(
#             attrs={'type': 'date', 'min': datetime.now().date()})

#     # Include fields from both Reservation and Customer models

#     customer_name = forms.CharField(
#         widget=forms.TextInput(attrs={'placeholder': 'Full name'})
#     )
#     email = forms.EmailField(
#         widget=forms.EmailInput(attrs={'placeholder': 'Email address'}))
#     phone_number = PhoneNumberField(
#         widget=forms.TextInput(attrs={'placeholder': ('+353')})
#     )

#     reserved_table = forms.ModelChoiceField(
#         # queryset=Table.objects.filter(reserved=False),
#         queryset=Table.objects.all(),
#         widget=forms.Select(attrs={'placeholder': 'Reserved Table'}),
#     )
#     # reserved_table = forms.ModelChoiceField(
#     #     queryset=Table.objects.all(),
#     #     widget=forms.Select(attrs={'placeholder': 'Reserved Table'}),
#     # )
    
#     # reservation_status = forms.ChoiceField(
#     #     choices=status_options,
#     #     widget=forms.Select(attrs={'placeholder': 'Reservation Status'}),
#     #     initial='awaiting confirmation'
#     # )    

#     class Meta:
#         model = Reservation
#         fields = ('customer_count', 'reserved_date', 'reserved_time_slot', 'customer_name', 'email', 'phone_number')
class BookingForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper(self)

    requested_date = forms.DateField(
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
            'reserved_time_slot')