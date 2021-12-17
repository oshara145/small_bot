import os
import telebot

bot = telebot.TeleBot('BOT_TOKEN')

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message,'Hello! Im {YOUR_NAME} How Are You')


  
  bot.polling()
