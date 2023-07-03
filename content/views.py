from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import GameEditForm, GameIntakeForm
from .models import Games, Genre


def game_catalog(request):
    query = request.GET.get('query', '')
    genre_id = request.GET.get('genre', 0)
    genres = Genre.objects.all()
    games = Games.objects.filter(on_sale=True)

    if genre_id:
        games = games.filter(genre_id=genre_id)

    if query:
        games = games.filter(Q(name__icontains=query) | Q(description__icontains=query))

    return render(request, 'games/game_catalog_page.html', {
        'games': games,
        'query': query,
        'genres': genres,
        'genre_id': int(genre_id)
    })

def game_page(request, game_key):
    game = get_object_or_404(Games, pk=game_key)
    related_games = Games.objects.filter(genre=game.genre).exclude(pk=game_key)[0:3]
    
    return render(request, 'games/game_page.html', {
        'game': game,
        'related_games': related_games
    })
    
@login_required
def game_intake(request):
    if request.method == 'POST':
        form = GameIntakeForm(request.POST, request.FILES)
        
        if form.is_valid():
            new_game = form.save() 

            return redirect('content:game_page', game_key=new_game.id)
    else:
        
        form = GameIntakeForm()
    
    return render(request, 'games/game_intake.html', {
        'form': form,
        'title': 'New Game'
    })

@login_required
def edit_game(request, game_key):
    game = get_object_or_404(Games, pk=game_key, developer=request.user)

    if request.method == 'POST':
        form = GameEditForm(request.POST, request.FILES, instance=game)

        if form.is_valid():
            form.save()

            return redirect('content:game_page', game_key=game.id)
    else:
        form = GameEditForm(instance=game)

    return render(request, 'games/edit_game.html', {
        'form': form,
        'title': 'Edit game info',
    })


@login_required
def remove_game(request, game_key):
    game = get_object_or_404(Games, pk=game_key, developer=request.user)
    game.delete()

    return redirect('user_dash:dash_home')