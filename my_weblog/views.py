from django.shortcuts import render, get_object_or_404
from .models import cheap_package, luxary_package, camping_package, post



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
    posts=post.objects.filter(status=1)
    context = {
        'posts':posts
    }

    return render(req,'my_weblog/blog-home.html',context=context)

def b_single(req):
    return render(req,'my_weblog/blog-single.html')

def test(req,pid):
    #posts = post.objects.get(id=pid)
    posts = get_object_or_404(post, pk=pid)#>>>>>> posts = post.objects.get(id=pid)
    context = {
        'post':posts.content
    }
    return render(req,'my_weblog/test.html',context=context)


