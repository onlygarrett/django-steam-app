from typing import Any
from django.db import models
from django.contrib.auth.models import User


class SteamTags(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Tags'
        
    def __str__(self):
        return self.name
    
    
class SteamGames(models.Model):

    steam_appid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    header_image = models.ImageField(upload_to='item_images', blank=True, null=True)
    price = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    release_date = models.DateTimeField(blank=True, null=True)
    developers = models.JSONField(default=list)
    tag = models.ForeignKey(SteamTags, related_name='items', on_delete=models.CASCADE)    
    on_sale = models.BooleanField(default=False)
    
    def __init__(self, steam_data: dict):
        super(SteamGames, self).__init__()
        for k, v in steam_data.items():
            setattr(self, k, v)
    
    class Meta:
        ordering = ('tag',)
        verbose_name_plural = 'SteamGames'
        
    def __str__(self):
        return self.name