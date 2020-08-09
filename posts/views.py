from django.shortcuts import render, get_object_or_404, redirect

from .models import Post
from .forms import PostForm


def index(request):
    last = Post.objects.order_by("-pub_date")[:1]
    posts = Post.objects.order_by("-pub_date")[1:10]
    return render(request, "index.html", {"last": last, "posts": posts})


def new_post(request):
    form = PostForm(request.POST or None, files=request.FILES or None)
    if request.method == "POST" and form.is_valid():
        new_post = form.save(commit=False)
        new_post.author = request.user
        new_post.save()
        return redirect("index")      
    return render(request, "new_post.html", {"form": form})


def post_view(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post.html", {"post": post})
