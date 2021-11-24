import telebot

def get_api_key():
    with open('API_KEY.txt', 'r') as file:
        return file.read()

bot = telebot.TeleBot(get_api_key())

if __name__ == '__main__':
    bot.polling()