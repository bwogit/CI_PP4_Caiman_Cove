# Imports
# 3rd party:
from django.urls import path
from .views import BlogList, AddComment
#Internal:
from . import views


urlpatterns = [
    path('blog_list/', views.BlogList.as_view(),
         name='blog_list'),
    path('add_comment/<int:pk>/', views.AddComment.as_view(),
         name='add_comment'),
    path('blog_detail/<int:pk>/', views.BlogDetail.as_view(),
         name='blog_detail'),
]
