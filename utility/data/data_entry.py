from datetime import datetime,timedelta
import json, pathlib
from typing import List
import tomli, tomlkit
from tomlkit import table, nl,comment


datetime.now().strftime
a = {'color': 'blue'}
a.update

DATA_PATH = pathlib.Path.cwd() / 'utility' / 'data'        
TAG_FILE = DATA_PATH / 'tags.toml'
DATA_FILE = DATA_PATH / 'game_data.toml'


def refresh_data():    
    yesterday_time = datetime.now() - timedelta(days=1)
    now1 = datetime.strftime(datetime.now(), '%Y%m%d')

    if TAG_FILE.exists():
        # update tag file
        with open("./utility/data/tags.toml", mode="rt", encoding="utf-8") as f:
            data = tomlkit.load(f)
            
        # grab tags
        tag_ids = []
        for key, value in data.items():
            tag_ids.append(value)
        
        if 'updated_on' in data.keys():
            hours_since_last_refresh = (yesterday_time - datetime.strptime(data['updated_on']['time'], '%Y%m%d')).total_seconds() / 3600
        else:
            hours_since_last_refresh = 0
        
        tb = table()
        tb.add("time", now1)
        data.add(nl()).add('updated_on', tb).add(comment("Most recent refresh"))
        
        if hours_since_last_refresh >= 48:
            data['updated_on']['time'] = now1
            with open("./utility/data/tags.toml", mode="wt", encoding="utf-8") as fp:
                tomlkit.dump(data, fp)
            
            write_data(tag_ids)
        elif not DATA_FILE.exists():
            write_data(tag_ids)
            with open("./utility/data/tags.toml", mode="wt", encoding="utf-8") as fp:
                tomlkit.dump(data, fp)
        else: 
            with open("./utility/data/tags.toml", mode="wt", encoding="utf-8") as fp:
                fp.close()
        
            # grab data
            write_data(tag_ids)
    else:
        return


def write_data(tag_ids: List[int]):
    # update data
    with open(DATA_FILE, mode="rt", encoding="utf-8") as f:
        game_data = tomlkit.load(f)    
    
    meow = {
        "user": {
            "player_x": {
            "symbol": "X",
            "color": "blue",
            "ai": "asdf"
            },
            "player_o": {
            "symbol": "O",
            "color": "green",
            "ai": "asdf"
            },
            "ai_skill": 0.85
        },
        "board_size": 3,
        "server": {"url": "https://tictactoe.example.com"}
        }

    data_output = tomlkit.document()
    for key, value in meow.values:
        if isinstance(value, dict):
            new_table = table()
            print(key)
            print(value)
            for key2, value2 in meow.items():
                print(key2)
                print(value2)
                new_table.add(key, value)
            data_output.add(nl()).add(key, new_table)
        else:
            data_output.append(key, value)
        
        data_output.add(nl())

    # Write out updated data
    with open(DATA_FILE, mode="wt", encoding="utf-8") as fp:
                tomlkit.dump(game_data, fp)

    return