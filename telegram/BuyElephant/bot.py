import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(content_types=['text'])
def lalala(message):
	bot.send_message(message.chat.id,'Усі кажуть ' + message.text + ', а ти купи слона')

bot.polling(none_stop=True)