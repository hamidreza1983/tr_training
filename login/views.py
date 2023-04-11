from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm, Captcha, EmailLoginForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse



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
                return HttpResponseRedirect('/')
        else:
            messages.add_message(req, messages.ERROR, 'not found this username')
            return HttpResponseRedirect('/login')

def Login_with_email(req):
    if req.user.is_authenticated:
        return redirect('/')
    if req.method == 'GET':
        form = EmailLoginForm()
        return render(req, 'login/email_login.html', {'form': form})
    if req.method == 'POST':
        form = EmailLoginForm(req.POST)
        if form.is_valid():
            email = req.POST['email']
            password = req.POST['password']
            try:
                username = User.objects.get(email=email.lower()).username
                user = authenticate(username=username, password=password)
                if user is not None:
                    login(req,user)
                    return HttpResponseRedirect(reverse('my_weblog:home'))
            except:
                messages.add_message(req, messages.ERROR, 'not found this email')
                return HttpResponseRedirect(reverse('login:login_with_email'))
        else:
            return HttpResponseRedirect (reverse('login:login_with_email'))

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