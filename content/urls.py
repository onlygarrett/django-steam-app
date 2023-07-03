from django.urls import path

from . import views

app_name = 'content'

urlpatterns = [
    path('', views.game_catalog, name='game_catalog'),
    path('game_intake/', views.game_intake, name='game_intake'),
    path('<int:game_key>/', views.game_page, name='game_page'),
    path('<int:game_key>/delete/', views.remove_game, name='remove_game'),
    path('<int:game_key>/edit/', views.edit_game, name='edit_game'),
]
