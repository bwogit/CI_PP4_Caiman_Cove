from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm
from django.views import View
from django.contrib.auth.decorators import login_required

# Create your views here.
class BlogList(View):
    def get(self, request):
        posts = Post.objects.filter(status=1)
        return render(request, 'blog/blog_list.html', {'posts': posts})

class BlogDetail(View):
    # A class to display the details of the blog #
    
    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=1)
        return render(request, 'blog/blog_detail.html', {'post': post})    

class AddComment(View):
    @login_required
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=1)
        name = request.user.username
        email = request.user.email
        body = request.POST.get('comment_body')
        comment = Comment(post=post, name=name, email=email, body=body)
        comment.save()
        return redirect('blog_detail', pk=post.pk)

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/add_comment.html', {'post': post})