from django.urls import path
from .views import BlogList, AddComment

urlpatterns = [
    path('blog_list', BlogList.as_view(), name='blog_list'),
    path('add_comment/<int:pk>/', AddComment.as_view(), name='add_comment'),
    
]

