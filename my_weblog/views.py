from django.shortcuts import render, get_object_or_404, redirect
from .models import cheap_package, luxary_package, camping_package, newsletter
from django.utils import timezone
from .models import contact
from .forms import ContactForm, NewsletterForm

def home(req):
    if req.method == 'POST':
        email = NewsletterForm(req.POST)
        if email.is_valid():
           email.save()
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
    if req.method == 'POST':
        form = ContactForm(req.POST)
        if form.is_valid():
            form.save()
    return render(req,'my_weblog/contact.html')