from django.urls import path , reverse_lazy
from . import views
      

app_name='login'

urlpatterns = [
    path('', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('signup', views.Signup, name='signup'),
]