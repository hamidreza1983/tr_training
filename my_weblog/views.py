from django.shortcuts import render, get_object_or_404, redirect
from .models import cheap_package, luxary_package, camping_package, newsletter
from django.utils import timezone
from .models import contact
from .forms import ContactForm

def home(req):
    if req.method == 'POST':
        news=newsletter()
        news.email = req.POST.get('emailaddress')
        news.save()
    cheap = cheap_package.objects.all()
    luxary= luxary_package.objects.all()
    camp= camping_package.objects.all()
    context={
        'cheap':cheap,
        'lux':luxary,
        'camp':camp,
    }
    return render(req,'my_weblog/index.html', context=context)

def about(req):
    return render(req,'my_weblog/about.html')

def Contact(req):
    return render(req,'my_weblog/contact.html')




def contact_us(req):
    posts = contact()
    forms = ContactForm()
    if req.method == 'POST':
        forms_edit = ContactForm(req.POST)
        if forms_edit.is_valid():
            posts.name = forms_edit.cleaned_data['name']
            posts.email = forms_edit.cleaned_data['email']
            posts.subject = forms_edit.cleaned_data['subject']
            posts.text = forms_edit.cleaned_data['text']
            posts.save()
    context = {
        'forms':forms
        }
    return render(req, 'my_weblog/contact.html', context=context) 

def test(req):
    forms = ContactForm()
    if req.method == 'POST':
        forms_edit = ContactForm(req.POST)
        if forms_edit.is_valid():
            forms_edit.save()
    context = {
        'forms':forms
        }
    return render(req, 'my_weblog/test.html', context=context) 