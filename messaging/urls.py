from django.urls import path

from . import views

app_name = 'messaging'

urlpatterns = [
    path('', views.message_home, name='message_home'),
    path('<int:message_key>/', views.message, name='message'),
    path('create/<int:game_key>/', views.new_message_group, name='create'),
]