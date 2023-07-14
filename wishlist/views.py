from locale import currency
from django.contrib.auth.decorators import login_required
from django.db.models import Model
from django.shortcuts import get_object_or_404, render

from content.models import Games
from wishlist.models import WishList


@login_required
def get_wishlist(request):
    current_list = WishList.get_or_create(request.user)
    
    return render(request, 'listview/wishlist_home.html', {
        'current_list': current_list
    })

@login_required
def add_to_wishlist(request, game_key):
    game = get_object_or_404(Games, pk=game_key)
    current_list = WishList.get_or_create(request.user)
    
    if not current_list.on_wishlist(game):
        
        current_list.game_list.add(game)
        current_list.save()
        
    return render(request, 'listview/wishlist_home.html', {
        'current_list': current_list
    })


@login_required
def remove_from_wishlist(request, game_key):
    game = get_object_or_404(Games, pk=game_key)
    current_list = WishList.get_or_create(request.user)
    
    if current_list.on_wishlist(game):
        current_list.game_list.remove(game)
        current_list.save()
        
    return render(request, 'listview/wishlist_home.html', {
        'current_list': current_list
    })