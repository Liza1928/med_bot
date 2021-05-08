import telebot

bot = telebot.TeleBot('1782400313:AAG_MajsWRTNuF9cNub9pleuwdvjo90PNZY')


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message)


bot.polling(none_stop=True, interval=0)
