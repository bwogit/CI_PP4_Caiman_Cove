from django.urls import path
from .views import ContactUser

urlpatterns = [
    path('contact/', ContactUser.as_view(), name='contact'),
    
]
