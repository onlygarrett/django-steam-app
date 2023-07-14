import os
import pathlib, tomllib
from tempfile import NamedTemporaryFile
from datetime import datetime

from urllib.request import urlopen
from django.core.files import File
from content.models import Games, Genre, Developer
from utility.models import SteamGames, SteamTags

# file paths of TOML files
DATA_PATH = pathlib.Path.cwd() / "utility" / "data" / "vault"
TAG_FILE = DATA_PATH / "tags.toml"
DATA_FILE = DATA_PATH / "game_data.toml"


def replace_old_data():
    
    # grabbing updated data file
    with open("./utility/data/vault/game_data.toml", mode="rb") as f:
        data = tomllib.load(f)
        
    _wipe_like_new()
        
    inner_data = list(data.values())
    
    for game in inner_data:           
        game_devs_per_game = []
        
        tag = SteamTags.objects.filter(name=game['tag']).first()
        if not tag:
            tag = SteamTags()
            tag.name = game['tag']
            tag.save()
                    
        del game['tag']
        
        genre = Genre.objects.filter(name=tag.name).first()
        if not genre:
            genre = Genre()
            genre.name = tag.name
            genre.save()
        
        for d in game['developers']:
            dev = Developer.objects.filter(name=d).first()
            if not dev:
                dev = Developer()
                dev.name = d
                dev.save()
            
            game_devs_per_game.append(dev)
                
        del game['developers'] 
        url = game['header_image']
        
        steam_game_data = SteamGames(game)
        steam_game_data.tag = tag
        steam_game_data.on_sale = (game['discount'] > 0)
        
        game = Games()
        
        game.name = steam_game_data.name
        game.description = steam_game_data.short_description[:100] + "..."
        
        game.image = steam_game_data.header_image
        game.price = steam_game_data.price
        game.on_sale = steam_game_data.on_sale
        game.discount = steam_game_data.discount
        release_date = datetime.strptime(steam_game_data.release_date, "%b %d, %Y")
        f_rd = datetime.strftime(release_date, "%Y%m%d")
        game.release_date = f_rd
        
        game.genre = genre
        game.save()
        img_temp = NamedTemporaryFile(delete=True)
        img_temp.write(urlopen(url).read())
        img_temp.flush()
        
        game.image.save(
            f"image_{game.name}.png",
            File(img_temp)
        )
        game.developers.set(game_devs_per_game)
        game.save()
    
        
    return
        
        
def _wipe_like_new():
    Developer.objects.all().delete()
    Genre.objects.all().delete()
    Games.objects.all().delete()