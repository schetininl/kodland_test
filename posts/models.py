from django.db import models

from tinymce.models import HTMLField


class Post(models.Model):
    title = models.CharField(max_length=80)
    text = HTMLField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)

 
