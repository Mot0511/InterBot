import telebot
import random



token = open('token.txt', 'r').read()
bot = telebot.TeleBot(token)

keyboard = telebot.types.ReplyKeyboardMarkup()
keyboard.row('Интересные сайты', 'Интересные картинки')

weather = ''
sites = ''


@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, я бот который может тебе показать интересные штуки!', reply_markup=keyboard)
    bot.send_photo(message.chat.id, open('icon.jpg', 'rb'))



@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text.lower() == 'интересные сайты':
        bot.send_message(message.chat.id, sites)

    elif message.text.lower() == 'интересные картинки':
        num = random.randint(0, 3)
        if num == 0:
            bot.send_photo(message.chat.id, open('img/ph1.png', 'rb'))

        elif num == 1:
            bot.send_photo(message.chat.id, open('img/ph2.png', 'rb'))

        elif num == 2:
            bot.send_photo(message.chat.id, open('img/ph3.png', 'rb'))


bot.polling()