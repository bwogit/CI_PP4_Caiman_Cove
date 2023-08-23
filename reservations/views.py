from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic, View
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic.edit import FormView
from django.views.generic import ListView
from django.views.generic import TemplateView
from .forms import BookingForm  # Import your BookingForm
from .models import Reservation
import datetime

def get_user_instance(request):
    """
    This function retrieves user details when the user is logged in
    """

    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user

# class Confirmed(TemplateView):
#     template_name = 'reservations/confirmed.html'


#class Bookings(LoginRequiredMixin, FormView):
class Bookings(View):
    """
    This view renders the booking form when a registered user accesses it, 
    automatically populating the email field with the user's email address.
    """
    template_name = 'reservations/reservation.html'  
    form_class = BookingForm
    success_url = 'confirmed'  

    # def get(self, request, *args, **kwargs):
    #     template_name = "reservations/reservation.html"
    #     booking_form = BookingForm()  # Create an instance of the form
    #     return render(request, template_name, {'booking_form': booking_form})
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


# Dispays the confirmation page upon a succesful booking



    # def form_valid(self, form):
    #     # Handle the form submission here
    #     cleaned_data = form.cleaned_data

    #     # Extract data from the cleaned_data dictionary
    #     customer_count = cleaned_data['customer_count']
    #     reserved_date = cleaned_data['reserved_date']
    #     reserved_time_slot = cleaned_data['reserved_time_slot']
    #     customer_name = cleaned_data['customer_name']
    #     email = cleaned_data['email']
    #     phone_number = cleaned_data['phone_number']

    #     # Check if the customer already exists
    #     customer, created = Customer.objects.get_or_create(
    #         customer_name=customer_name,
    #         email=email,
    #         phone=phone_number
    #     )

    #     # Create a new reservation instance with the extracted data and customer
    #     reservation = Reservation(
    #         customer_count=customer_count,
    #         reserved_date=reserved_date,
    #         reserved_time_slot=reserved_time_slot,
    #         customer=customer,
    #     )
    #     # Set reservation status to 'awaiting confirmation'
        
    #     print("Before setting status:", reservation.reservation_status)
    #     reservation.reservation_status = 'awaiting confirmation'
    #     print("After setting status:", reservation.reservation_status)

    #     return redirect('confirmed')


# class BookingList(ListView):
#     model = Reservation
#     template_name = 'reservations/booking_list.html'
#     context_object_name = 'bookings'
#     paginate_by = 4

#     def get_queryset(self):
#         # Get all reservations for the current user's customer
#         return Reservation.objects.filter(customer__email=self.request.user.email).order_by('-reservation_time')

class BookingList(generic.ListView):
    """
    This view will display all the bookings
    a particular user has made
    """
    model = Reservation
    queryset = Reservation.objects.filter().order_by('-reservation_time')
    template_name = 'booking_list.html'
    paginated_by = 4

    def get(self, request, *args, **kwargs):

        booking = Reservation.objects.all()
        paginator = Paginator(Reservation.objects.filter(user=request.user), 4)
        page = request.GET.get('page')
        booking_page = paginator.get_page(page)
        today = datetime.datetime.now().date()

        for date in booking:
            if date.reserved_date < today:
                date.status = 'Booking Expired'

        if request.user.is_authenticated:
            bookings = Reservation.objects.filter(user=request.user)
            return render(
                request,
                'reservations/booking_list.html',
                {
                    'booking': booking,
                    'bookings': bookings,
                    'booking_page': booking_page})
        else:
            return redirect('accounts/login.html')