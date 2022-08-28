
from dataclasses import fields
from lib2to3.pygram import python_symbols
from django import forms
from .models import Comment, Post
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ( 'detail', ) 

class BlogForm(forms.ModelForm):


    class Meta:
        model = Post
        fields = [ 'tag', 'title','intro', 'body']

class UpdateForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [ 'tag', 'title','intro', 'body', 'id']    
