from django.shortcuts import render, get_object_or_404
from .models import cheap_package, luxary_package, camping_package
from django.utils import timezone



def home(req):
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

def contact(req):
    return render(req,'my_weblog/contact.html')




def blog_2(req):
    return 'hello'


