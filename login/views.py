from django.shortcuts import render
from django.contrib.auth import authenticate
from blog.models import post

def login(req):
    if req.method == 'POST':
        username = req.POST['username']
        password = req.POST['password']
        print (username)
        print (password)
        user = authenticate(username=username, password=password)
        if user is not None:
            posts = post.objects.filter(status=1)
            return render(req,'blog/blog-home.html', {'posts':posts})
        else:
            return render(req,'my_weblog/index.html')
    return render(req,'login/login.html')
    
    

    
