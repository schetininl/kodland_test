from django.db import models
from django import forms
from django.forms import ModelForm, Textarea

from .models import Post

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'image']
        labels = {
            'title': '',
            'text': '',
            'image': (''),
        }
