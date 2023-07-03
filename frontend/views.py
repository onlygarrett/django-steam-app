from django.shortcuts import render, redirect

from content.models import Games, Genre

from .forms import UserSignUpForm

#homepage
def home(request):
    games = Games.objects.filter(on_sale=True)[0:6]
    genres = Genre.objects.all()
    
    return render(request, 'general/home.html', {
        'genres': genres,
        'games': games
    })

#contact page
def contact(request):
    return render(request, 'general/contact.html')

#user signup
def user_signup(request):
    if request.method == 'POST':
        form = UserSignUpForm(request.POST)

        if form.is_valid():
            form.save()

            return redirect('/login/')
    else:
        form = UserSignUpForm()

    return render(request, 'general/user_signup.html', {
        'form': form
    })