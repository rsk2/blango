from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
import logging

logger=logging.getLogger(__name__)

def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now())
    logger.debug("Got %d posts", len(posts))
    logger.debug(index.__name__)
    return render(request, "blog/index.html", {"posts": posts})
  

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    logger.info(
      "Created comment on Post %d for user %s", post.pk, request.user
    )

    return render(request, "blog/post-detail.html", {"post": post})