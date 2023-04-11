from django.urls import path 
from . import views

app_name='login'

urlpatterns = [
    path('', views.Login, name='login'),
    path('emaillogin', views.Login_with_email, name='login_with_email'),
    path('logout', views.Logout, name='logout'),
    path('signup', views.Signup, name='signup'),
]
