from django.shortcuts import render
from .models import cheap_package

def home(req):
    context={
        'city1':cheap_package.objects.filter(id=1)
    }
    return render(req,'my_weblog/index.html', context=context)

def about(req):
    return render(req,'my_weblog/about.html')

def contact(req):
    return render(req,'my_weblog/contact.html')

def b_home(req):
    return render(req,'my_weblog/blog-home.html')

def b_single(req):
    return render(req,'my_weblog/blog-single.html')

