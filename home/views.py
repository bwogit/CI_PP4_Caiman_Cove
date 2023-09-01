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


@login_required
def change_password(request):
    """
    A view for changing the password, accessible only for logged-in users
    taken from Django 
    """
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request,
                             'Your password was successfully updated!')
            return redirect('profile')  # Redirect to the user's profile page
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {'form': form})
