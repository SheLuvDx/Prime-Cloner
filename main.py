mytitle = "PrimeCloner - Developed by Primelus"
from os import remove, system
system("title "+mytitle)
import discord
import asyncio
from colorama import AnsiToWin32, Fore, init, Style
from prime import Clone
import webbrowser
import requests
client = discord.Client()
from time import sleep
import os
import json



cls = lambda: os.system('cls')
cls()

init()

with open('config.json') as config_file: data = json.load(config_file)

# Load .env

token = data['token']








# the banner
banner = (f"""{Fore.RED}
██████╗ ██████╗ ██╗███╗   ███╗███████╗     ██████╗██╗      ██████╗ ███╗   ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██║████╗ ████║██╔════╝    ██╔════╝██║     ██╔═══██╗████╗  ██║██╔════╝██╔══██╗
██████╔╝██████╔╝██║██╔████╔██║█████╗      ██║     ██║     ██║   ██║██╔██╗ ██║█████╗  ██████╔╝
██╔═══╝ ██╔══██╗██║██║╚██╔╝██║██╔══╝      ██║     ██║     ██║   ██║██║╚██╗██║██╔══╝  ██╔══██╗
██║     ██║  ██║██║██║ ╚═╝ ██║███████╗    ╚██████╗███████╗╚██████╔╝██║ ╚████║███████╗██║  ██║
╚═╝     ╚═╝  ╚═╝╚═╝╚═╝     ╚═╝╚══════╝     ╚═════╝╚══════╝ ╚═════╝ ╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝
                                                                                             
                        {Style.RESET_ALL}
                                            {Fore.MAGENTA}Developed by: Primelus{Style.RESET_ALL}
        """) 


print(f'{banner}')



# Discord Shit
head = {'Authorization': str(token)}
src = requests.get('https://discordapp.com/api/v6/users/@me', headers=head)
if src.status_code == 200:
    print(f'{Fore.GREEN}[+] Your Token Is Valid {Style.RESET_ALL}')
    sleep(4)
else:
    print(f'{Fore.RED}[-] Your Token Is Invalid {Style.RESET_ALL}')
    sleep(4)
    exit()


def mainanswer():
    cls()
    print(f'{banner}')

    headers = {'Authorization': token, 'Content-Type': 'application/json'}
    r = requests.get('https://discord.com/api/v6/users/@me', headers=headers)
    if r.status_code == 200:
        userName = r.json()['username'] + '#' + r.json()['discriminator']
        userID = r.json()['id']

    print(f'''                                    Logged As {userName} ({userID})''')
    print('\n')
    print(f'                            [1] > {Fore.RED}Clone Server{Style.RESET_ALL}                 [2] > {Fore.MAGENTA}Support Server{Style.RESET_ALL}')
    print('\n')
    print('\n')


    answer = input('\033[1;00m[\033[91m>\033[1;00m]\033[91m\033[00m Choose : ')
    if answer == '1':
        cloner()
    elif answer == '2':
        prime()
    else:
        print('Incorrect selection, please choose a number')
        mainanswer()

def prime():
    webbrowser.open_new('https://discord.gg/prime')
    cls()
    mainanswer()


def cloner():
    cls()
    print(f'{banner}')
    print('\n')
    guild_s = input('Your Server ID That You Wnat To Copy > ')
    guild = input('Your Server ID To Copy The Server In Thare > ')
    input_guild_id = guild_s
    output_guild_id = guild  
    print('Wanne Create automaticly an template? (y/n)')
    answer = input('Choose :')


    cls()


    @client.event
    async def on_ready():
        cls()
        print(f'{banner}')
        print('\n')
        print(f"Logged In as : {client.user}")
        print("Cloning Server")
        guild_from = client.get_guild(int(input_guild_id))
        guild_to = client.get_guild(int(output_guild_id))
        await Clone.roles_delete(guild_to)
        await Clone.channels_delete(guild_to)
        await Clone.roles_create(guild_to, guild_from)
        await Clone.categories_create(guild_to, guild_from)
        await Clone.channels_create(guild_to, guild_from)
        await Clone.guild_edit(guild_to, guild_from)
        if answer == 'y':
            await Clone.guild_template(guild_to)
        else:
            pass
        await asyncio.sleep(5)
        cls()
        mainanswer()
    client.run(token, bot=False)



mainanswer()
