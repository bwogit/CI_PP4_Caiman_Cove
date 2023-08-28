from django.contrib import messages
from django.shortcuts import render
from django.core.paginator import Paginator
from .forms import BookingForm
from .models import Reservation
from django.urls import reverse_lazy
from django.views import generic, View
import datetime


class Bookings(View):
    """
    This view renders the booking form when a registered user accesses it, 
    automatically populating the email field with the user's email address.
    """
    template_name = 'reservations/reservation.html'
    form_class = BookingForm
    
    def get(self, request, *args, **kwargs):
        """
        Retrieves users email and inputs into email field
        """
        if request.user.is_authenticated:
            email = request.user.email
            booking_form = BookingForm(initial={'email': email})
        else:
            booking_form = BookingForm()
        return render(request, 'reservations/reservation.html', {'booking_form': booking_form})

    def post(self, request):
        """
        Validates the provided information 
        format and then saves it to the database.
        """
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(request, "Booking successful, awaiting confirmation")
            return render(request, 'reservations/confirmed.html')

        return render(request, 'reservations/reservation.html', {'booking_form': booking_form})


class Confirmed(generic.DetailView):
    """
    This view will display confirmation on a successful booking
    """
    template_name = 'reservations/confirmed.html'

    def get(self, request):
        return render(request, 'reservations/confirmed.html')


class BookingList(generic.ListView):
    """
    A custom implementation of BookingList view.
    """
    model = Reservation
    template_name = 'reservations/booking_list.html'
    paginate_by = 4

    def get_queryset(self):
        """
        Return a filtered queryset based on user authentication.
        """
        queryset = Reservation.objects.filter().order_by('-reservation_time')
        user = self.request.user
        if user.is_authenticated:
            queryset = queryset.filter(user=user)
            today = datetime.datetime.now().date()
            for booking in queryset:
                if booking.reserved_date < today:
                    booking.status = 'Booking Expired'
        return queryset

    def get_context_data(self, **kwargs):
        """
        Add additional context data to the template.
        """
        context = super().get_context_data(**kwargs)
        context['bookings'] = self.get_queryset()
        return context


class EditBooking(generic.UpdateView):
    model = Reservation
    form_class = BookingForm
    template_name = 'reservations/edit_booking.html'
    success_url = reverse_lazy('booking_list')  # Redirect after successful update

    def get_queryset(self):
        return super().get_queryset().filter(user=self.request.user)

    def form_valid(self, form):
        response = super().form_valid(form)
        messages.success(self.request, "Your reservation has been updated.")
        return response

    def get_success_url(self):
        return self.success_url  # Return the URL for redirect


class DeleteBooking(generic.DeleteView):
    """
    A class to handle deleting reservations
    """
    model = Reservation
    template_name = 'reservations/delete_booking.html'
    success_url = reverse_lazy('booking_list')  # Redirect after successful deletion

    def get_queryset(self):
        # Make sure the user can only delete their own reservations
        return super().get_queryset().filter(user=self.request.user)

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Reservation deleted successfully.")
        return super().delete(request, *args, **kwargs)
