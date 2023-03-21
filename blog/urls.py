from django.urls import path
from .views import b_home, b_single



app_name = 'blog'
urlpatterns = [
    path('', b_home, name= 'blog-home'),
    path('<int:pid>', b_single, name='blog-single' )
]