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
    tag = models.ForeignKey(SteamTags, related_name='items', on_delete=models.CASCADE)
    steam_appid = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    short_description = models.TextField(blank=True, null=True)
    header_image = models.ImageField(upload_to='item_images', blank=True, null=True)
    price_overview = models.FloatField()
    on_sale = models.BooleanField(default=False)
    developer = models.CharField(max_length=255)
    release_date = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        ordering = ('tag',)
        verbose_name_plural = 'SteamGames'
        
    def __str__(self):
        return self.name