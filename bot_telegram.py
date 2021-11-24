import telebot

def get_api_key():
    with open('API_KEY.txt', 'r') as file:
        return file.read()

bot = telebot.TeleBot(get_api_key())

def is_true(msg):
    return True

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'oioi, tudo bem com você? aqui é do Rareneger')
    default_message(message)

@bot.message_handler(func=is_true)
def default_message(message):
    bot.reply_to(message, 'default message')

if __name__ == '__main__':
    bot.polling()