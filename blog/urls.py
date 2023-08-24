from django.urls import path
from . import views
from .views import BlogList, AddComment

urlpatterns = [
    path('blog_list/', views.BlogList.as_view(), name='blog_list'),
    path('add_comment/<int:pk>/', views.AddComment.as_view(), name='add_comment'),
    path('blog_detail', views.BlogDetails.as_view(), name='add_comment')
    
]

