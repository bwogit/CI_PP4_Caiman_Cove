from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    """
    A form to create comments on blog posts.
    It is based on the Comment model and provides validation.
    """
    class Meta:
        model = Comment
        #fields = ('title', 'slug', 'featured_image', 'excerpt', 'content', 'status')
        fields = ('body',)