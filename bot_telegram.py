import telebot

def get_api_key():
    with open('API_KEY.txt', 'r') as file:
        return file.read()

bot = telebot.TeleBot(get_api_key())

to_register = []

def is_true(msg):
    return True

def is_register(message):
    chat_id = message.chat.id
    if chat_id in to_register:
        to_register.remove(chat_id)
        return True
    else:
        return False

@bot.message_handler(func=is_register)
def register_chat(message):
    bot.reply_to(message, 'Número registrado com sucesso!')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, 'oioi, tudo bem com você? aqui é do Rareneger')
    default_message(message)

@bot.message_handler(commands=['cadastrar'])
def register_message(message):
    to_register.append(message.chat.id)
    bot.reply_to(message, 'Agora envie o seu número de atendimento')

@bot.message_handler(func=is_true)
def default_message(message):
    bot.reply_to(message, 'Para cadastrar este chat para receber a confirmação de seu atendimento clique em /cadastrar')

if __name__ == '__main__':
    bot.polling()