from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = ('title', 'slug', 'featured_image', 'excerpt', 'content', 'status')
        fields = ('body',)