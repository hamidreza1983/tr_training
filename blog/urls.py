from django.urls import path
from .views import b_home, b_single, search



app_name = 'blog'
urlpatterns = [
    path('', b_home, name= 'blog-home'),
    path('<int:pid>/', b_single, name='blog-single' ),
    path('category/<str:cat>', b_home, name='blog-home' ),
    path('tag/<str:tag>', b_home, name='blog-home' ),
    path('<str:username>', b_home, name='author' ),
    path('search/', search, name = 'search')
]