from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from captcha.fields import CaptchaField

class Captcha(forms.Form):
    captcha = CaptchaField()
    class Meta:
        fields = ['captcha']

class UserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")#

#class AuthenticationForm(AuthenticationForm):
#    email = forms.EmailField(required=False)
#    class Meta:
#        model = User
#        fields = ("email", "password")

class EmailLoginForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(max_length=20)
    class Meta:
        model = User
        fields = ('email', 'password')
        