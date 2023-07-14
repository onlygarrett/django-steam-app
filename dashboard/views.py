from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from content.models import Games, Genre

@login_required
def dash_home(request):
    games = Games.objects.all()
    genres = Genre.objects.all()

    return render(request, 'user_dash/dash_home.html', {
        'games': games,
        'genres': genres
    })