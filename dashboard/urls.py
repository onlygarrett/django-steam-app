from django.urls import path

from . import views

app_name = 'user_dash'

urlpatterns = [
    path('', views.dash_home, name='dash_home'),
]