from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect, reverse
from django.core.paginator import Paginator
from django.views.generic.edit import FormView, UpdateView, DeleteView
from django.views.generic import ListView, TemplateView
from .forms import BookingForm  # Import your BookingForm
from .models import Reservation, Table
import datetime
from django.urls import reverse_lazy

def get_user_instance(request):
    """
    This function retrieves user details when the user is logged in
    """

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


class Bookings(View):
    """
    This view renders the booking form when a registered user accesses it, 
    automatically populating the email field with the user's email address.
    """
    template_name = 'reservations/reservation.html'  
    form_class = BookingForm
    success_url = 'confirmed'  

    
    def get(self, request, *args, **kwargs):
        """
        Retrieves users email and inputs into email field
        """
        if request.user.is_authenticated:
            email = request.user.email
            booking_form = BookingForm(initial={'email': email})
        else:
            booking_form = BookingForm()
        return render(request, 'reservations/reservation.html',
                      {'booking_form': booking_form})


    def post(self, request):
        """
        Checks that the provided info is valid format
        and then posts to database
        """
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(
                request, "Booking succesful, awaiting confirmation")
            return render(request, 'reservations/confirmed.html')

        return render(request, 'reservations/reservation.html',
                      {'booking_form': booking_form})

        
     

class Confirmed(generic.DetailView):
    """
    This view will display confirmation on a successful booking
    """
    template_name = 'reservations/confirmed.html'

    def get(self, request):
            return render(request, 'reservations/confirmed.html')



# class BookingList(generic.ListView):
#     """
    
#     """
#     model = Reservation
#     queryset = Reservation.objects.filter().order_by('-reservation_time')
#     #queryset = Reservation.objects.select_related('table').filter(user=request.user).order_by('-reservation_time')
#     template_name = 'booking_list.html'
#     paginated_by = 4

#     def get(self, request, *args, **kwargs):

#         booking = self.queryset
#         paginator = Paginator(Reservation.objects.filter(user=request.user), 4)
#         page = request.GET.get('page')
#         booking_page = paginator.get_page(page)
#         today = datetime.datetime.now().date()

#         for date in booking:
#             if date.reserved_date < today:
#                 date.status = 'Booking Expired'

#         if request.user.is_authenticated:
#             bookings = Reservation.objects.filter(user=request.user)
#             return render(
#                 request,
#                 'reservations/booking_list.html',
#                 {
#                     'booking': booking,
#                     'bookings': bookings,
#                     'booking_page': booking_page})
#         else:
#             return redirect('accounts/login.html')
class BookingList(generic.ListView):
    model = Reservation
    queryset = Reservation.objects.filter().order_by('-reservation_time')
    template_name = 'booking_list.html'
    paginate_by = 4

    def get(self, request, *args, **kwargs):
        today = datetime.datetime.now().date()

        if request.user.is_authenticated:
            bookings = self.queryset.filter(user=request.user)
            paginator = Paginator(bookings, self.paginate_by)
            page = request.GET.get('page')
            booking_page = paginator.get_page(page)

            for date in bookings:
                if date.reserved_date < today:
                    date.status = 'Booking Expired'

            return render(
                request,
                'reservations/booking_list.html',
                {
                    'booking': bookings,
                    'booking_page': booking_page
                }
            )
        else:
            return redirect('accounts/login.html')

      
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from .models import Reservation
from .forms import BookingForm

class EditBooking(UpdateView):
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

class DeleteBooking(DeleteView):
    """
    A class to handle deleteing reservations
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