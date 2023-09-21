import telebot

ID = "661262775"
bot = telebot.TeleBot("6296022389:AAH84-tKh_LlcGUaspHpvmaqVgHF2yz8hmI")  

def start_bot():
    bot.send_message(ID, '!BOT STARTED!')
    print("Bot launched!")
