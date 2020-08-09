from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=80)
    text = models.TextField()
    pub_date = models.DateTimeField("date published", auto_now_add=True)
    image = models.ImageField(upload_to="posts/", blank=True, null=True)
