import telebot
import config
from telebot import types
import random


bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	sti = open('static/Welcome.tgs', 'rb')
	bot.send_sticker(message.chat.id, sti)
	markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	item1 = types.KeyboardButton('🎲 Рандомне число')
	item2 = types.KeyboardButton('😊 Як справи?')
	markup.add(item1, item2)
	bot.send_message(message.chat.id, "Welcome, {0.first_name}!\nЯ - бот <b>{1.first_name}</b>, давай спілкуватися.".format(message.from_user, bot.get_me()),
		parse_mode='html', reply_markup=markup)

@bot.message_handler(content_types=['text'])
def lalala(message):
	if message.chat.type == 'private':
		if message.text == '🎲 Рандомне число':
			bot.send_message(message.chat.id, str(random.randint(0,100)))
		elif message.text == '😊 Як справи?' :

			markup = types.InlineKeyboardMarkup(row_width=2)
			item1 = types.InlineKeyboardButton('Добре', callback_data='good')
			item2 = types.InlineKeyboardButton('Неособо', callback_data='bad')
			markup.add(item1, item2)
			bot.send_message(message.chat.id, 'Vse okey', reply_markup=markup)
		else:
			bot.send_message(message.chat.id, 'WTFFFFFFF?')

@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                bot.send_message(call.message.chat.id, 'Ну й добре шо добре😊')
            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Shit happens 😢')
 
            # remove inline buttons
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="",
                reply_markup=None)
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="test2020")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)