from pyexpat import model
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.db import models

from content.models import Games


class WishList(models.Model):
    owner = models.ForeignKey(
        User, verbose_name="User", related_name="wishlist", on_delete=models.CASCADE
    )
    game_list = models.ManyToManyField(
        Games, related_name="items"
    )

    def on_wishlist(self, game: Games) -> bool:
        return (game in self.game_list.all())

    @classmethod
    def get_or_create(cls, owner: User):
        current_list = WishList.objects.filter(owner=owner).first()
        if not current_list:
            current_list = WishList.objects.create(owner=owner)
            current_list.save()

        return current_list
