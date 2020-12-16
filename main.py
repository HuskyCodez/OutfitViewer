import string, random, json, os, ctypes, shutil, time, datetime, threading
from colorama import Fore, init
import requests

################# Colors ##################
init()
reset = str(Fore.RESET)
red = str(Fore.RED)
green = str(Fore.GREEN)
blue = str(Fore.LIGHTCYAN_EX)
light_blue = str(Fore.LIGHTBLUE_EX)
light_red = str(Fore.LIGHTRED_EX)
yellow = str(Fore.YELLOW)
light_yellow = str(Fore.LIGHTYELLOW_EX)
################# Colors ##################

downloaded = 0
outfit_URL = ('https://avatar.roblox.com/v1/users/{}/outfits?page=1&itemsPerPage=100')
conv_URL = "https://api.roblox.com/users/get-by-username?username="
id_URL = "https://api.roblox.com/users/"

def mode_user():
    user = str(input("Username?: "))
    conv = conv_URL + user
    response = requests.get(conv).json()
    user_id = response["Id"]
    scrape(user, user_id)


def mode_id():
    id = input("User ID?: ")
    user = id_URL + str(id)
    response = requests.get(user).json()
    name = response["Username"]
    scrape(name, id)


def scrape(user, plr_id):
    os.mkdir('Outfits')
    global downloaded
    print(f"\n{light_blue}Getting outfits of {light_red}{user}{reset} | {light_blue}ID: {light_red}{plr_id}{reset}")
    print("")
    response = requests.get(outfit_URL.format(plr_id)).json()
    outfit_count = response["total"]
    start = datetime.datetime.now()
    for a in response["data"]:
        outfit_name = a["name"]
        outfit_id = a["id"]
        t = datetime.datetime.now()
        thumb_URL = 'https://www.roblox.com/outfit-thumbnail/image?userOutfitId={}&width=420&height=420&format=png'.format(outfit_id)
        r = requests.get(thumb_URL)
        open("Outfits/{}.png".format(outfit_name),"wb").write(r.content)
        elapsed_time = datetime.datetime.now() - t
        downloaded += 1
        print(f'{light_yellow}Outfit Name: {light_red}{outfit_name}{reset} | {Fore.LIGHTBLACK_EX}ID: {outfit_id}{reset} | {light_yellow}Time Taken: {light_red}{round(elapsed_time.total_seconds() * 1000)}ms{reset}')
    elapsed_time = datetime.datetime.now() - start
    print(f"\n{light_blue}Got outfits of {light_red}{user}{reset} | {light_blue}ID: {light_red}{plr_id}{reset}")
    print(f"{light_blue}Downloaded: {light_red}[{downloaded}{reset}/{light_red}{outfit_count}]{light_blue} outfits{reset} | {light_blue}Total time taken: {light_red}{round(elapsed_time.total_seconds())}s{reset}")


if __name__ == "__main__":
    try:
        ctypes.windll.kernel32.SetConsoleTitleW("RBX Outfit Viewer by Husky_Playz")
        try:
            shutil.rmtree("Outfits")
            print("{}Deleted old outfit/s{}".format(yellow, reset))
        except:
            print("{}Outfits does not exist, skipping{}".format(yellow, reset))
        print('')
        mode = int(input("Search via [1] Username [2] User ID: "))
        if mode == 1:
            mode_user()
            print("{}\nOpened outfit viewer GUI{}".format(yellow, reset))
            os.system("gui.py")
        elif mode == 2:
            mode_id()
            print("{}\nOpened outfit viewer GUI{}".format(yellow, reset))
            os.system("gui.py")

    except Exception as e:
        print("{}ERROR ==> {}{}".format(red, reset, e))
        input()