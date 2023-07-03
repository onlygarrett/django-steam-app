from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=255)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Genres'
        
    def __str__(self):
        return self.name
    
    
class Games(models.Model):
    genre = models.ForeignKey(Genre, related_name='items', on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null=True)
    price = models.FloatField()
    on_sale = models.BooleanField(default=False)
    developer = models.ForeignKey(User, related_name='items', on_delete=models.CASCADE)
    release_date = models.DateTimeField(blank=True, null=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Games'
        
    def __str__(self):
        return self.name