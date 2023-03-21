from django.shortcuts import render, get_object_or_404
from .models import post



def b_home(req):
    posts=post.objects.filter(status=1)
    context = {
        'posts':posts
    }

    return render(req,'blog/blog-home.html',context=context)

def b_single(req, pid):
    posts=get_object_or_404(post, pk=pid, status= True)
    posts.counted_viwes += 1
    posts.save()
    context = {
        'post':posts
    }
    return render(req,'blog/blog-single.html',context=context)

# Create your views here.
