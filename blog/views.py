from django.shortcuts import render, get_object_or_404
from .models import post



def b_home(req):
    posts=post.objects.filter(status=1)
    context = {
        'posts':posts
    }

    return render(req,'blog/blog-home.html', context=context)

def b_single(req, pid):
    total = post.objects.all()
    posts=get_object_or_404(post, pk=pid, status=1)
    posts.counted_viwes += 1
    posts.save()
    if pid == len(total):
        prev = get_object_or_404(post, pk=pid-1, status=1)
        next = None
    elif pid == 1 :
        prev = None
        next = get_object_or_404(post, pk=pid+1, status=1)
    else:
        prev = get_object_or_404(post, pk=pid-1, status=1)
        next = get_object_or_404(post, pk=pid+1, status=1)

    context = {
        'post' : posts,
        'next' : next,
        'prev' : prev,
    }
    return render(req,'blog/blog-single.html', context=context)

