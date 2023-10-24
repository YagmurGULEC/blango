from django.shortcuts import render
from .models import Post
from django.utils import timezone

def index(request):
    posts=Post.objects.all()
    return render(request,"blog/index.html",{'posts':posts})

