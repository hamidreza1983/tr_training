from django.shortcuts import render

def home(req):
    return render(req,'my_weblog/index.html')

def about(req):
    return render(req,'my_weblog/about.html')

def contact(req):
    return render(req,'my_weblog/contact.html')

def b_home(req):
    return render(req,'my_weblog/blog-home.html')

def b_single(req):
    return render(req,'my_weblog/blog-single.html')



