from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
class BlogListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog_list.html', {'posts': posts})