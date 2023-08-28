from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    """
    A form to gather user contact information and message.
    It is based on the Contact model and provides validation.
    """
    class Meta:
        model = Contact
        fields = ['email', 'name', 'message']
