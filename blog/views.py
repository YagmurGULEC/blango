from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404

def index(request):
    posts=Post.objects.all()
    return render(request,"blog/post-list.html",{'posts':posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    return render(request, "blog/post-detail.html", {"post":
    post})