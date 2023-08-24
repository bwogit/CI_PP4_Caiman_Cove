from django.urls import path
from .views import BlogList, AddComment

urlpatterns = [
    path('blog/blog_list/', BlogList.as_view(), name='blog_list'),
    path('blog/<int:pk>/add_comment/', AddComment.as_view(), name='add_comment'),
    
]