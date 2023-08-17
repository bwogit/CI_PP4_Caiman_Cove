
# Imports
from django.shortcuts import render



def index(request):
    """
    a view to display the homepage
    """
    return render(request, 'home/index.html')