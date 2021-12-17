import os
import telebot

bot = telebot.TeleBot('BOT_TOKEN')

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message,'Hello! Im {YOUR_NAME} How Are You')

@bot.message_handler(commands=['how'])
def send_message(message):
  bot.send_message(message, 'Im Fine 🙂')
  
  bot.polling()
