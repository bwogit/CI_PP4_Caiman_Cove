from django.urls import path
from .views import ContactUser, ContactGreeting

urlpatterns = [
    path('contact_us/', ContactUser.as_view(), name='contact_us'),
    path('contact_greeting/', ContactGreeting.as_view(), name='contact_greeting'),
]
