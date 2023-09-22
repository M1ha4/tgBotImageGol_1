import telebot
from telebot import types
bot=telebot.TeleBot('6510543135:AAEdIWHEkR_ncIOQ-bvVhOKTJ3sHF4PCOsk')

@bot.message_handler(commands=['start'])
def start(message):
    mess=f"Привет, {message.from_user.first_name}.\nЭтот бот отправляет фотографии животных и звуки, которые они издают.\n" \
         f"Выбери животное:\n" \
         f"1)/lev\n" \
         f"2)/volk\n" \
         f"3)/sobaka\n" \
         f"4)/koshka\n" \
         f"5)/osel\n" \
         f"6)/lagushka"

    bot.send_message(message.chat.id, mess, parse_mode='html')

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    lev = types.KeyboardButton("/Лев")
    volk = types.KeyboardButton("/Волк")
    sobaka = types.KeyboardButton("/Собака")
    koshka = types.KeyboardButton("/Кошка")
    osel = types.KeyboardButton("/Осел")
    lagushka = types.KeyboardButton("/Лягушка")
    markup.add(lev, volk, sobaka, koshka, osel, lagushka)


@bot.message_handler(commands=['lev'])
def lev(message):
    bot.send_message(message.chat.id, "Лев")
    photo_lev = open('lev.jpg', 'rb')
    bot.send_photo(message.chat.id, photo_lev)
    voice = ""
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['volk'])
def lev(message):
    bot.send_message(message.chat.id, "Лев")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEEYI5iTCYHKPkx6v2rIbJfAAFZfoxKlPwAArkXAAK-klBJwmt_557uyEIjBA')
    voice = open('https://zvukogram.com/zvuk/29599/', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['sobaka'])
def lev(message):
    bot.send_message(message.chat.id, "Лев")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEEYI5iTCYHKPkx6v2rIbJfAAFZfoxKlPwAArkXAAK-klBJwmt_557uyEIjBA')
    voice = open('https://zvukogram.com/zvuk/29599/', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['koshka'])
def lev(message):
    bot.send_message(message.chat.id, "Лев")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEEYI5iTCYHKPkx6v2rIbJfAAFZfoxKlPwAArkXAAK-klBJwmt_557uyEIjBA')
    voice = open('https://zvukogram.com/zvuk/29599/', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['osel'])
def lev(message):
    bot.send_message(message.chat.id, "Лев")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEEYI5iTCYHKPkx6v2rIbJfAAFZfoxKlPwAArkXAAK-klBJwmt_557uyEIjBA')
    voice = open('https://zvukogram.com/zvuk/29599/', 'rb')
    bot.send_voice(message.chat.id, voice)

@bot.message_handler(commands=['lagushka'])
def lev(message):
    bot.send_message(message.chat.id, "Лев")
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEEYI5iTCYHKPkx6v2rIbJfAAFZfoxKlPwAArkXAAK-klBJwmt_557uyEIjBA')
    voice = open('https://zvukogram.com/zvuk/29599/', 'rb')
    bot.send_voice(message.chat.id, voice)
bot.infinity_polling()