from django.urls import path
from .views import *



app_name='my_weblog'


urlpatterns = [
    path('', home, name= 'home'),
    path('about/', about, name= 'about'),
    path('contact', Contact, name= 'contact'),
]