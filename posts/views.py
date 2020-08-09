from django.shortcuts import render, get_object_or_404

from .models import Post


def index(request):
    last = Post.objects.order_by("-pub_date")[:1]
    posts = Post.objects.order_by("-pub_date")[1:10]
    return render(request, "index.html", {"last": last, "posts": posts})


def new_post(request):
    return render(request, "new_post.html", {"test": "test"})

def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post.html", {"post": post})