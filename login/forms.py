from django import forms
from captcha.fields import CaptchaField
from django.contrib.auth.models import User

class Captcha(forms.Form):
    captcha = CaptchaField()
    class Meta:
        fields = ['captcha']