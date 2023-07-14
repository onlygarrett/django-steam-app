# django-steam-app

This is a django app project that grabs the top 60 or so games on Steam and allows user's to create wishlists and message other user's about them.

#### These are the main features of this app:
 - Homepage listing all current games
 - Search feature
 - A few genre features
 - A messaging service that between other interested users in a game
 - Wishlist Service
 
 ---
## Dependencies

This app mainly runs with `django`, `pillow`, `requests`, `tomllkit`, and a few others found in `requirements.txt`



### Data Acquisition:
The game data for this app is grabbed using [Steam's Store API](store.steampowered.com), to which it is parsed down and stored in a TOML file in `game_data.toml`.

*ALL* Game data is refreshed based on a django management command that can be ran in the docker containter with `./repopulate_data.sh`

I did have this working with a cronjob in the docker container but didn't include that in the main app.

When `repopulate_data` is ran the `game_tags.toml` file is grabbed and based on the timestamp will repopulate data if the last refresh is >48 hours.

This is also where you can add/remove genre's to show in the app.

___

## Usage

Clone the repo
Create a virtualenv in the base directory, activate it, and install requirements with

```bash
virtualenv venv
source .venv/bin/activate
pip install -r requirements.txt
```

run the docker files
```bash
docker compose up -d
```

Once it's up and running create the initial migrations and run the base command for data
```bash
docker exec -it <container> bash
root@21599c12325f:/code# python manage.py makemigrations
root@21599c12325f:/code# python manage.py migrate
root@21599c12325f:/code# ./repopulate_data.sh
```
___