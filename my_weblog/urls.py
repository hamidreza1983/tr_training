from django.urls import path
from .views import *



app_name='my_weblog'


urlpatterns = [
    path('', home, name= 'home'),
    path('about', about, name= 'about'),
    path('contact', contact, name= 'contact'),
    path('blog-home', b_home, name= 'blog-home'),
    path('blog-single', b_single, name= 'blog-single'),
]