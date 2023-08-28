from django.shortcuts import render


def home(request):
    """
    a view to display the homepage
    """
    return render(request, 'home/index.html')


def custom_404_view(request, exception):
    return render(request, '404.html', status=404)
