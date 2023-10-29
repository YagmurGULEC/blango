from .models import Post
from django.utils import timezone
from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
import logging
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
# adding logger
logger = logging.getLogger(__name__)

# view caching for 300 seconds (5 mins)


# @cache_page(300)
# @vary_on_cookie
def index(request):
    # from django.http import HttpResponse
    # return HttpResponse(str(request.user).encode("ascii"))
    # to optimize the query
    posts = Post.objects.all().select_related(
        "author").defer("modified_at", "created_at")

    # posts = Post.objects.all()
    # or
    """
    posts = Post.objects.all().select_related("author").only(
        "title", "summary", "content", "author", "published_at", "slug")
    """

    logger.info("Number of posts %s", len(posts))

    return render(request, "blog/post-list.html", {'posts': posts})

# ip address connected to django


def get_ip(request):
    return HttpResponse(request.META['REMOTE_ADDR'])


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)
            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None
    return render(request, "blog/post-detail.html", {"post":
                                                     post, "comment_form": comment_form})
