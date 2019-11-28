import config
import telebot

bot = telebot.TeleBot(config.token)
chat_id = '655197990'


@bot.message_handler(content_types=['text'])
def repeat_all_messages(message):
    bot.send_message(message.chat_id, message.text)


if __name__ == '__main__':
    bot.polling(none_stop=True)
