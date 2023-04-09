from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from .forms import Captcha
from django.contrib.auth.decorators import login_required



def Login(req):
    if req.user.is_authenticated:
        return redirect('/')
    if req.method == 'GET':
        form = AuthenticationForm()
        return render(req, 'login/login.html', {'form': form})
    if req.method == 'POST':
        form = AuthenticationForm(request=req, data=req.POST)
        if form.is_valid():
            user = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(req,username=user,password=password)
            if user is not None:
                login(req,user)
                return redirect('/')
        else:
            messages.add_message(req, messages.ERROR, 'not found this username')

@login_required     
def Logout(req):
    logout(req)
    return redirect('/')


def Signup(req):
    if not req.user.is_authenticated:
        if req.method == "POST":
            form = UserCreationForm(req.POST)
            if form.is_valid():
                form.save()
                return redirect('/')
            else:
                messages.add_message(req, messages.ERROR, 'password not correct ')
        form = UserCreationForm()
        context = {
            'form' : form
        }
        return render(req, 'login/signup.html',context=context)
    return redirect('/')