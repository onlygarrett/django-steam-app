from django.db import models
from django.contrib.auth.models import User


class Genre(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Genres"

    def __str__(self):
        return self.name


class Developer(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Developers"

    def __str__(self):
        return self.name


class Games(models.Model):
    genre = models.ForeignKey(Genre, related_name="items", on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="item_images", blank=True, null=True)
    price = models.FloatField(default=0)
    on_sale = models.BooleanField(default=False)
    discount = models.FloatField(default=0)
    developers = models.ManyToManyField(Developer, related_name="developers")
    release_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        ordering = ("name",)
        verbose_name_plural = "Games"

    def __str__(self):
        return self.name
