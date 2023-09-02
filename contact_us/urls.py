# Imports
# 3rd party:
from django.urls import path
# Internal:
from .views import ContactUser

urlpatterns = [
    path('contact_us/', ContactUser.as_view(), name='contact_us'),
    ]

