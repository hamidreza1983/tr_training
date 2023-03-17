from django.shortcuts import render, get_object_or_404
from .models import cheap_package, luxary_package, camping_package, post
from django.utils import timezone



def home(req):
    cheap = cheap_package.objects.all()
    luxary= luxary_package.objects.all()
    camp= camping_package.objects.all()
    context={
        'cheap':cheap,
        'lux':luxary,
        'camp':camp,
    }
    return render(req,'my_weblog/index.html', context=context)

def about(req):
    return render(req,'my_weblog/about.html')

def contact(req):
    return render(req,'my_weblog/contact.html')

def b_home(req):
    posts=post.objects.filter(published_date__lte=timezone.now())
    context = {
        'posts':posts
    }

    return render(req,'my_weblog/blog-home.html',context=context)

def b_single(req, pid):
    posts=get_object_or_404(post, pk=pid, status= 1)
    posts.counted_viwes += 1
    posts.save()
    context = {
        'post':posts
    }
    return render(req,'my_weblog/blog-single.html',context=context)


def blog_2(req):
    return 'hello'


