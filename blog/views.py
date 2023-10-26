from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404,redirect
from .forms import CommentForm
import logging

#adding logger
logger = logging.getLogger('__name__')

def index(request):
    posts=Post.objects.all()
    logger.info("Number of posts %s",len(posts))

    return render(request,"blog/post-list.html",{'posts':posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        if request.method=="POST":
            comment_form=CommentForm(request.POST)
            if comment_form.is_valid():
                comment=comment_form.save(commit=False)
                comment.content_object=post
                comment.creator=request.user
                comment.save()
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form=None
    return render(request, "blog/post-detail.html", {"post":
    post,"comment_form":comment_form})