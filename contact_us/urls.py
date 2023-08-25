from django.urls import path
from .views import ContactUserView

urlpatterns = [
    path('contact/', ContactUser.as_view(), name='contact'),
    
]
