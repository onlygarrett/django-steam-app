import pathlib
from datetime import datetime, timedelta
from typing import List

import requests
import tomlkit

from steamapp.settings import (REQUIRED_DATA, STEAM_APP_API_URL,
                               STEAM_TAG_SEARCH_API_URL)

# file paths of TOML files
DATA_PATH = pathlib.Path.cwd() / "utility" / "data" / "vault"
TAG_FILE = DATA_PATH / "tags.toml"
DATA_FILE = DATA_PATH / "game_data.toml"


def start_refresh_if_needed() -> bool:
    yesterday_time = datetime.now() - timedelta(days=1)
    now1 = datetime.strftime(datetime.now(), "%Y%m%d")

    if TAG_FILE.exists():
        # update tag file
        with open("./utility/data/vault/tags.toml", mode="r", encoding="utf-8") as f:
            data = tomlkit.load(f)

        # grab tags
        tag_ids = []
        for key, value in data["tags"].items():
            tag_ids.append({key: value})

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
            with open("./utility/data/vault/tags.toml", mode="wt", encoding="utf-8") as fp:
                tomlkit.dump(data, fp)
            write_data(tag_ids)
            return True
        
        elif not DATA_FILE.exists():
            write_data(tag_ids)
            with open("./utility/data/vault/tags.toml", mode="wt", encoding="utf-8") as fp:
                tomlkit.dump(data, fp)
            return True

    else:
        return False


def write_data(tag_ids: List[dict]) -> None:
    game_ids = _tag_list_helper(tag_ids=tag_ids)

    new_game_data = tomlkit.document()
    main_game_info = {}
    tag_label_for_game = "N/A"

    for game_tag_list in game_ids:
        for app_id in game_tag_list:
            game_table = tomlkit.table()
            if type(app_id) == str:
                tag_label_for_game = app_id
                continue

            game_response = requests.get(STEAM_APP_API_URL.substitute(app_id=app_id))
            game_json = game_response.json()
            game_info_card = game_json.get(str(app_id))
            game_info = game_info_card.get("data")

            for _ in REQUIRED_DATA:
                game_data_point = game_info.get(_)
                if not game_data_point or isinstance(game_data_point, dict):
                    if _ == "release_date":
                        main_game_info.update({"release_date": game_data_point["date"]})

                    elif _ == "price_overview":
                        if game_data_point:
                            main_game_info.update({"price": game_data_point["final"]})
                            main_game_info.update(
                                {"discount": game_data_point["discount_percent"]}
                            )

                    elif _ == "developers":
                        main_game_info.update({"developer": game_data_point[0]})

                else:
                    main_game_info.update({_: game_data_point})

            main_game_info.update({"tag": tag_label_for_game})

            game_table.update(main_game_info)
            try:
                new_game_data.append(str(app_id), game_table)
            except tomlkit.exceptions.KeyAlreadyPresent:
                pass

    with open("./utility/data/vault/game_data.toml", mode="w", encoding="utf-8") as fp:
        tomlkit.dump(new_game_data, fp)

    return


def _tag_list_helper(tag_ids: List[dict]) -> List[str]:
    i = 0
    game_ids_with_pre_tag = []
    for tag_dict in tag_ids:
        tag_label = list(tag_dict.keys())[i]
        id = tag_dict[tag_label]
        resp = requests.get(STEAM_TAG_SEARCH_API_URL + str(id))
        resp_list = resp.json()["appids"].copy()
        resp_list.insert(0, tag_label)
        game_ids_with_pre_tag.append(resp_list)
        i += i

    return game_ids_with_pre_tag
