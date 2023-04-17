from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserCreationForm, Captcha
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings



def Login(req):
    if req.user.is_authenticated:
        return redirect('/')
    if req.method == 'GET':
        form = AuthenticationForm()
        return render(req, 'login/login.html', {'form': form})
    if req.method == 'POST':
        form = AuthenticationForm(request=req, data=req.POST)
        user = req.POST['username']
        password = req.POST['password']
        if '@' in user:
            email = req.POST['username']
            username = User.objects.get(email=email.lower()).username
            user = authenticate(username=username, password=password)
            if user is not None:
                login(req,user)
                return HttpResponseRedirect(reverse('my_weblog:home'))
            else:
                messages.add_message(req, messages.ERROR, 'username/email or password is incorrect')
                return HttpResponseRedirect(reverse('login:login'))
        else:
            user = authenticate(username=user, password=password)
            if user is not None:
                login(req,user)
                return HttpResponseRedirect(reverse('my_weblog:home'))
            else:
                messages.add_message(req, messages.ERROR, 'username/email or password is incorrect')
                return redirect('/login')

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
                messages.add_message(req, messages.ERROR, 'compelet all fileds and strong password')
        form = UserCreationForm()
        context = {
            'form' : form
        }
        return render(req, 'login/signup.html',context=context)
    return redirect('/')