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

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs.update({
            'placeholder': 'Введите название статьи'
        })
        