from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib import messages


def home(request):
    """
    a view to display the homepage
    """
    return render(request, 'home/index.html')
