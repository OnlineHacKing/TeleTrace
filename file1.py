import telebot

ID = "661262775"
bot = telebot.TeleBot("6264887049:AAHVKKKZA7bVnzi7VdML1WH_PGq4mRqpfrY")  

def start_bot():
    bot.send_message(ID, '!BOT STARTED!')
    print("Bot launched!")
