import telebot

TOKEN = "5479352740:AAE5DNBb6F8xHoPb02_kbwGMHjW30T9RL6I"
bot = telebot.TeleBot(TOKEN)
# @bot.message_handler(commands=['start','help']) - обрабатываем комманды
#     def handle_start_help(message)


@bot.message_handler(commands=['start','help'])
def send_welcom(message):
    bot.send_message(message.chat.id, f'Welcom, {message.chat.username}')

bot.polling(none_stop=True)
