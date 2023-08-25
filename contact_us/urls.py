from django.urls import path
from .views import ContactUser

urlpatterns = [
    path('contact_us/', ContactUser.as_view(), name='contact_us'),
    
]
