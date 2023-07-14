import json
from django.contrib import admin

from .models import Genre, Games, Developer

admin.site.register(Genre)
admin.site.register(Games)
admin.site.register(Developer)
