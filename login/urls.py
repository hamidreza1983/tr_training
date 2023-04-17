from django.urls import path , reverse_lazy
from . import views
from django.contrib.auth.views import PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
    
    
    
    

app_name='login'

urlpatterns = [
    path('', views.Login, name='login'),
    path('logout', views.Logout, name='logout'),
    path('signup', views.Signup, name='signup'),
    path('password_reset/', PasswordResetView.as_view(),name='password_reset'),
    path('password_reset/done/', PasswordResetDoneView.as_view(),name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    path('password_reset_complete/',PasswordResetCompleteView.as_view(),name='password_reset_complete'),
]