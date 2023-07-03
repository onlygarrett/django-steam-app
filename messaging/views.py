from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

from content.models import Games

from .forms import MessageForm
from .models import MessageService

@login_required
def new_message_group(request, game_key):
    game = get_object_or_404(Games, pk=game_key)

    if game.developer == request.user:
        return redirect('user_dash:dash_home')
    
    message_groups = MessageService.objects.filter(game=game).filter(members__in=[request.user.id])

    if message_groups:
        return redirect('messaging:message', pk=message_groups.first().id)

    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            message_group = MessageService.objects.create(game=game)
            message_group.members.add(request.user)
            message_group.members.add(game.developer)
            message_group.save()

            message = form.save(commit=False)
            message.message_group = message_group
            message.messager = request.user
            message.save()

            return redirect('content:game_page', game_key=game_key)
    else:
        form = MessageForm()
    
    return render(request, 'messages/new_message_group.html', {
        'form': form
    })

@login_required
def message_home(request):
    message_groups = MessageService.objects.filter(members__in=[request.user.id])

    return render(request, 'messages/message_home.html', {
        'message_groups': message_groups
    })

@login_required
def message(request, message_key):
    message_group = MessageService.objects.filter(members__in=[request.user.id]).get(pk=message_key)

    if request.method == 'POST':
        form = MessageForm(request.POST)

        if form.is_valid():
            message = form.save(commit=False)
            message.message_group = message_group
            message.messager = request.user
            message.save()

            message_group.save()

            return redirect('messaging:message', message_key=message_key)
    else:
        form = MessageForm()

    return render(request, 'messages/message.html', {
        'message_group': message_group,
        'form': form
    })