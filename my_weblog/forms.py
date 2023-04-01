from django import forms
from .models import contact, newsletter

class ContactForm(forms.ModelForm):
    name = forms.CharField(max_length=255)
    email = forms.EmailField()
    subject = forms.CharField(max_length=255)
    text = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = contact
        fields = ['name', 'email', 'subject', 'text']


class NewsletterForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = newsletter
        fields = ['email']
