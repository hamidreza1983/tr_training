from django.shortcuts import render, get_object_or_404
from .models import post, comment
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .forms import CommentForm


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
    if req.method == "POST":
        form = CommentForm(req.POST)
        if form.is_valid():
            form.save()
    form = CommentForm()
    total = post.objects.filter(status=1)
    posts=get_object_or_404(post, id=pid, status=1)
    com = comment.objects.filter(post=posts.id, status=1) 
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
        'form' : form,
        'comments' : com,
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