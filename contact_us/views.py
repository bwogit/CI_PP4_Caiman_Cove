from django.shortcuts import render
from django.views import View
from .forms import ContactForm

class ContactUser(View):
    template_name = 'contact_user.html'

    def get(self, request, *args, **kwargs):
        # Check if the user is logged in
        if request.user.is_authenticated:
            initial_data = {'email': request.user.email}
        else:
            initial_data = {}

        contact_form = ContactForm(initial=initial_data)
        return render(request, self.template_name, {'contact_form': contact_form})
