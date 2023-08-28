from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.core.paginator import Paginator


class BlogList(View):
    """
    A class to display a list of blog posts.
    """
    def get(self, request):
        posts = Post.objects.filter(status=1)
        paginator = Paginator(posts, 2)  # Display 2 posts per page
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        return render(request, 'blog/blog_list.html', {'page_obj': page_obj})


class BlogDetail(View):
    """
    A class to display the details of a blog post.
    """

    def get(self, request, pk):
        post = get_object_or_404(Post, pk=pk, status=1)
        comment_form = CommentForm()  # Create an instance of the form
        comments = post.comments.filter(approved=True).order_by('-created_on')
        return render(request, 'blog/blog_detail.html',
                      {'post': post, 'comment_form': comment_form})


class AddComment(LoginRequiredMixin, View):
    """
    A view to add comments to a blog post.
    Requires login.
    """

    login_url = 'login'

    def post(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk, status=1)
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
            messages.success(request, 'Comment pending approval')
        else:
            messages.error(request, 'Please try again')

        return redirect('blog_detail', pk=post.pk)

    def get(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        return render(request, 'blog/add_comment.html', {'post': post})
