from discord_webhook import DiscordWebhook
import random
import ctypes
import os
import getpass
from time import sleep


class ConsoleColors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    BOLD = '\033[1m'
    RED = '\033[31m'

words = ("Do you think Dean has seen this yet", "Jack called me a child once", "funni IP - 127.00.1", "John is still protesting", "Faze Babatundae got no-scoped", "github/127-00-1", "This is skidded shhhh", "https://cdn.discordapp.com/attachments/837567318044180510/908751113057095790/video0.mov")
word = random.choice(words)
user = getpass.getuser()

ctypes.windll.kernel32.SetConsoleTitleW(f"Webhook raper | 1.0 | skidded professionally by benJ | {word} | current user {user}")

os.system("cls")
print(ConsoleColors.RED + '''

                         /$$       /$$                           /$$                                                             
                        | $$      | $$                          | $$                                                             
 /$$  /$$  /$$  /$$$$$$ | $$$$$$$ | $$$$$$$   /$$$$$$   /$$$$$$ | $$   /$$        /$$$$$$  /$$$$$$   /$$$$$$   /$$$$$$   /$$$$$$ 
| $$ | $$ | $$ /$$__  $$| $$__  $$| $$__  $$ /$$__  $$ /$$__  $$| $$  /$$/       /$$__  $$|____  $$ /$$__  $$ /$$__  $$ /$$__  $$
| $$ | $$ | $$| $$$$$$$$| $$  \ $$| $$  \ $$| $$  \ $$| $$  \ $$| $$$$$$/       | $$  \__/ /$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/
| $$ | $$ | $$| $$_____/| $$  | $$| $$  | $$| $$  | $$| $$  | $$| $$_  $$       | $$      /$$__  $$| $$  | $$| $$_____/| $$      
|  $$$$$/$$$$/|  $$$$$$$| $$$$$$$/| $$  | $$|  $$$$$$/|  $$$$$$/| $$ \  $$      | $$     |  $$$$$$$| $$$$$$$/|  $$$$$$$| $$      
 \_____/\___/  \_______/|_______/ |__/  |__/ \______/  \______/ |__/  \__/      |__/      \_______/| $$____/  \_______/|__/      
                                                                                                   | $$                          
                                                                                                   | $$                          
                                                                                                   |__/                          
DISCORD: benJ#6787                                                                                    
      ''')

webmessage = input(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "        [SPAMMER] " + ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Message >> " + ConsoleColors.WARNING)
print()
weblink = input(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "        [SPAMMER] " + ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Webhook Link >> " + ConsoleColors.WARNING)
print()
webname = input(ConsoleColors.BOLD + ConsoleColors.OKBLUE + "        [SPAMMER] " + ConsoleColors.BOLD + ConsoleColors.OKGREEN + "Webhook Name >> " + ConsoleColors.WARNING)
print()


webhook = DiscordWebhook(url=weblink, content=webmessage, rate_limit_retry=True,
                         username=webname)

i = 1
while i < 6:
    response = webhook.execute()
    print(ConsoleColors.BOLD + ConsoleColors.OKGREEN + "        [SUCCESS] " + ConsoleColors.BOLD + ConsoleColors.RED +'a message sent successfully.')
