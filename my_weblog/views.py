from django.shortcuts import render, get_object_or_404, redirect
from .models import cheap_package, luxary_package, camping_package, newsletter
from django.utils import timezone
from .models import contact



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
    con = contact()
    if req.method == "POST":
       print('post')
       con.name = req.POST.get('name')
       con.email = req.POST.get('email')
       con.subject = req.POST.get('subject')
       con.text = req.POST.get('message')
       con.save()