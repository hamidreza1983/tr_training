from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from blog.models import post
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages

def Login(req):
    if not req.user.is_authenticated:
        if req.method == 'POST':
            form = AuthenticationForm(req, req.POST)
            if form.is_valid():
                user = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(req,username=user,password=password)
                if user is not None:
                    login(req,user)
                    return redirect('/blog')
                else:
                    messages.add_message(req, messages.WARNING, 'not found this username')
            else:
                messages.add_message(req, messages.ERROR, 'input date not possible')
        form = AuthenticationForm()
        context = {
            'form':form,
        }
        return render(req,'login/login.html', context=context)
    else:
        redirect(req,'/')
    
def Logout(req):
    if req.user.is_authenticated:
        logout(req)
    return redirect('/')


def Signup(req):
    if req.user.is_authenticated:
        logout(req)
    return redirect('/')
    
