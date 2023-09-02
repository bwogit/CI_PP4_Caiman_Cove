# Imports
# 3rd Party:
from django.shortcuts import render


def home(request):
    """
    a view to display the homepage
    """
    return render(request, 'home/index.html')
