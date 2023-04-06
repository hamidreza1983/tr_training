from django import forms
from .models import contact, newsletter
from captcha.fields import CaptchaField

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)
    captcha = CaptchaField()

    class Meta:
        model = contact
        fields = ['name', 'email', 'subject', 'text', 'captcha']


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField()
    captcha = CaptchaField()

    class Meta:
        model = newsletter
        fields = ['email', 'captcha']
