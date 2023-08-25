from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ContactForm

class ContactUser(LoginRequiredMixin, View):
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

    class ContactGreeting(View):
    template_name = 'contact_greeting.html'

    def get(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            # If the user is not authenticated, display a message
            messages.info(request, 'Before you can leave a message, please log in.')
            # Redirect the user to the contact form page
            return HttpResponseRedirect(reverse('contact_us'))
        return render(request, self.template_name)