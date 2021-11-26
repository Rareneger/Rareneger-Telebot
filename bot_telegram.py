import telebot
import sys
from urllib3.exceptions import ReadTimeoutError 
from requests.exceptions import ReadTimeout, ConnectionError

bot = telebot.TeleBot(sys.argv[1])

to_register = []

def is_true(msg):
    return True

def is_register(message):
    chat_id = message.chat.id
    if chat_id in to_register:
        return True
    else:
        return False

def mark_registered(message):
    to_register.remove(message.chat.id)

def mark_to_register(message):
    to_register.append(message.chat.id)

def is_number_valid(message):
    if message.text.isdigit() and len(message.text) in (11, 12):
        return True
    return False

@bot.message_handler(func=is_register)
def register_chat(message):
    if is_number_valid(message):
        mark_registered(message)
        bot.reply_to(message, 'Número registrado com sucesso!')
    else:
        bot.reply_to(message, 'O número não é válido, digite novamente')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'oioi, tudo bem com você? aqui é do Rareneger')
    default_message(message)

@bot.message_handler(commands=['cadastrar'])
def register_message(message):
    mark_to_register(message)
    bot.reply_to(message, 'Agora envie o seu número de atendimento')

@bot.message_handler(func=is_true)
def default_message(message):
    bot.reply_to(message, 'Para cadastrar este chat para receber a confirmação de seu atendimento clique em /cadastrar')

if __name__ == '__main__':
    in_error = False
    while True:
        try:
            bot.polling()
        except (ReadTimeoutError, ReadTimeout, ConnectionError):
            pass
