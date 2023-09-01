from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('change_password/', views.change_password, name='change_password'),
]
