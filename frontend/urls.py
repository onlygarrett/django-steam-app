from django.urls import path
from django.contrib.auth import views as authentication
from .forms import UserLoginForm

from . import views

app_name = 'frontend'

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.user_signup, name='user_signup'),
    path('login/', authentication.LoginView.as_view(
            template_name='general/login.html',
            authentication_form=UserLoginForm
        ), name='login')
]
