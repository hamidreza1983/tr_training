from django.shortcuts import render, get_object_or_404
from .models import post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def b_home(req, cat=None, username=None, tag=None):
    posts = post.objects.filter(status=1)
    
    if cat:
        posts = posts.filter(category__name=cat)
    
    if username:
        posts = posts.filter(author__username=username)
    
    if tag : 
        posts = posts.filter(tags__name=tag)
    
    posts = Paginator(posts,3)
    try :
        page_number = req.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
   
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

def search(request):
    posts = post.objects.filter(status=1)
    if key := request.GET.get('search'):
        posts = posts.filter(content__contains=key)
    context = {
        'posts':posts
    }
    return render(request, 'blog/blog-home.html', context=context)