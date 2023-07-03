from django.contrib.auth.models import User
from django.db import models

from content.models import Games

class MessageService(models.Model):
    game = models.ForeignKey(Games, related_name='message_groups', on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name='message_groups')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-last_modified',)
    
class Message(models.Model):
    message_group = models.ForeignKey(MessageService, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    messager = models.ForeignKey(User, related_name='created_messages', on_delete=models.CASCADE)