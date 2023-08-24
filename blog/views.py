from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
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
        comment_form = CommentForm()  # Create an instance of the form
        comments = post.comments.filter(approved=True).order_by('-created_on')
        return render(request, 'blog/blog_detail.html', {'post': post, 'comment_form': comment_form})    

class AddComment(View):
    @login_required
    # def post(self, request, pk):
    #     post = get_object_or_404(Post, pk=pk, status=1)
    #     name = request.user.username
    #     email = request.user.email
    #     body = request.POST.get('comment_body')
    #     comment = Comment(post=post, name=name, email=email, body=body)
    #     comment.save()
    #     return redirect('blog_detail', pk=post.pk)
    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=1)
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.name = request.user.username
            comment.email = request.user.email
            comment.save()
        return redirect('blog_detail', pk=post.pk)

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/add_comment.html', {'post': post})