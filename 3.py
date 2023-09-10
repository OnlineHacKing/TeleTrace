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
        print('1')

    elif choice == 2:
        # Code for choice 2 (Instagram cheat)
        print('1')

    elif choice == 3:
        # Code for choice 3 (Brawl stars)
        print('1')

    elif choice == 4:
        # Code for choice 4 (Acquaintance)
        print('1')

    else:
        print('Invalid choice')
else:
    print('Sorry, the entered number does not contain 12')
