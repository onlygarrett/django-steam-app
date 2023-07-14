from django.urls import path

from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.get_wishlist, name='get_wishlist'),
    path('<int:game_key>/', views.add_to_wishlist, name='add_to_wishlist'),
    path('<int:game_key>/delete/', views.remove_from_wishlist, name='remove_from_wishlist')
]
