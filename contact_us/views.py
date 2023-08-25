from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContactForm

class ContactUserView(LoginRequiredMixin, View):
    template_name = 'contact_us.html'

    def get(self, request, *args, **kwargs):
        # Check if the user is logged in
        # if request.user.is_authenticated:
        #     initial_data = {'email': request.user.email}
        # else:
        #     initial_data = {}
        user = request.user
        contact_form = ContactForm(initial={'email': user.email, 'name': user.username} if user.is_authenticated else {})
        return render(request, self.template_name, {'contact_form': contact_form})

        contact_form = ContactForm(initial=initial_data)
        return render(request, self.template_name, {'contact_form': contact_form})
