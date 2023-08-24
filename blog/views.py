from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import PostForm
from django.contrib.auth.decorators import login_required

# Create your views here.
class BlogListView(View):
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog_list.html', {'posts': posts})

    @login_required
    def add_comment_to_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        name = request.user.username
        email = request.user.email
        body = request.POST['comment_body']
        comment = Comment(post=post, name=name, email=email, body=body)
        comment.save()
        return redirect('blog_detail', pk=post.pk)
    return render(request, 'blog/add_comment_to_post.html', {'post': post})