import telebot
import random
bot= telebot.TeleBot('5031561834:AAHEnfRQio8IK5hADaGFXC0uRSd5Vi_Egbo')
from telebot import types
f = open('facts.txt', 'r', encoding='UTF-8')
facts = f.read().split('\n')
f.close()

t = open('thinks.txt', 'r', encoding='UTF-8')
thinks = t.read().split('\n')
t.close()

@bot.message_handler(commands=["start"])
def start(m,res=False):
    markup = types.ReplyKeyboardMarkup(realize_keyboard = True)
    bot.send_message(m.chat.id,"Отправь мне любое слово, и я найду его значение на Wikipedia")
    item1=types.KeyboardButton('Факт')
    item2=types.KeyboardButton('Поговорка')
    markup.add(item1)
    markup.add(item2)
    bot.send_message(m.chat.id, "Нажми: \nФакт для получения интересного факта\nПоговорка — для получения мудрой цитаты ", reply_markup=markup)
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text.strip()=='Факт':
        answer=random.choice(facts)
    elif message.text.strip()=='Поговорка':
        answer=random.choice(thinks)

    bot.send_message(message.chat.id, answer)


bot.polling(none_stop=True,interval=0)