from datetime import datetime, timedelta
from typing import List
from steamapp.settings import STEAM_TAG_SEARCH_API_URL, STEAM_APP_API_URL, REQUIRED_DATA
import tomlkit

import requests
import pathlib


DATA_PATH = pathlib.Path.cwd() / "utility" / "data"
TAG_FILE = DATA_PATH / "tags.toml"
DATA_FILE = DATA_PATH / "game_data.toml"
data = dict


def refresh_data():
    yesterday_time = datetime.now() - timedelta(days=1)
    now1 = datetime.strftime(datetime.now(), "%Y%m%d")

    if TAG_FILE.exists():
        # update tag file
        with open("./utility/data/tags.toml", mode="r", encoding="utf-8") as f:
            data = tomlkit.load(f)

        # grab tags
        tag_ids = []
        for key, value in data['tags'].items():
            tag_ids.append({key:value})

        if "updated_on" in data.keys():
            hours_since_last_refresh = (
                yesterday_time - datetime.strptime(data["updated_on"]["time"], "%Y%m%d")
            ).total_seconds() / 3600
        else:
            hours_since_last_refresh = 0
            tb = tomlkit.table()
            tb.add("time", now1)
            data.add(tomlkit.nl()).add("updated_on", tb).add(
                tomlkit.comment("Most recent refresh")
            )

        if hours_since_last_refresh >= 48:
            data["updated_on"]["time"] = now1
            with open("./utility/data/tags.toml", mode="wt", encoding="utf-8") as fp:
                tomlkit.dump(data, fp)

            write_data(tag_ids)
        elif not DATA_FILE.exists():

            write_data(tag_ids)
            with open("./utility/data/tags.toml", mode="wt", encoding="utf-8") as fp:
                tomlkit.dump(data, fp)
        
    else:
        return


def write_data(tag_ids: List[dict]):
    with open("./utility/data/game_data.toml", mode="rt", encoding="utf-8") as f:
        data = tomlkit.load(f)
        data.clear()
            
    game_ids = []
    main_game_info = {}
    
    i = 0
    for tag_dict in tag_ids:
        
        tag_label = list(tag_dict.keys())[i]
        id = tag_dict[tag_label]
        resp = requests.get(STEAM_TAG_SEARCH_API_URL + str(id))
        resp_list = resp.json()['appids'].copy()
        resp_list.insert(0, tag_label)
        game_ids.append(resp_list)
        i+=i
    
    
    for game_tag_list in game_ids:
        for app_id in game_tag_list:
            if type(app_id) == str:
                tag_label_for_game = app_id
            else:
                resp_2 = requests.get(STEAM_APP_API_URL.substitute(app_id=app_id))
                game_info = resp_2.json()
                inner_game_info = game_info[list(game_info.keys())[0]]
                for key, value in inner_game_info.items():
                    if key != 'data':
                        continue
                
                    main_game_info = value.copy()
                    
            
            new_table = tomlkit.table()
            for key, value in main_game_info.items():
                if not value:
                    main_game_info[key] = 'N/a'
                try:
                    
                    if isinstance(value, dict) and "price" in list(value.keys())[0]:
                        new_table.add(key, value['final_formatted'])
                        data.add('price_overview', new_table)
                        for key, value in value['price_overview'].items():
                            if key == 'discount_percent' and value > 0:
                                new_table.add('on_sale', True)
                                data.add('discounts', new_table)
                            
                    elif key in REQUIRED_DATA:
                        new_table.add(key, value)
                        new_table.add('tag', tag_label_for_game)
                    
                        data.add(str(app_id), new_table)
                
                    data.add(tomlkit.nl()).add(str(app_id), new_table)
                except tomlkit.exceptions.KeyAlreadyPresent:
                    pass
    
    
    
    # dict_no_none = _remove_none_values(final_game_results, data)                
    with open("./utility/data/game_data.toml", mode="wt", encoding="utf-8") as fp:
        tomlkit.dump(data, fp)

    return
