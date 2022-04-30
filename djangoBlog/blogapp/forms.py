from xml.etree.ElementTree import Comment
from django import forms
from .models import Comments

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['name', 'email', 'body']