import os
import telebot

bot = telebot.Telebot('2144282821:AAEBYkPU6dLOFrbO3Kf8FDmIOzqX7ircTkI')

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message,'Hello! Im Oshara How Are You')

@bot.message_handler(commands=['how])
def send_message(message):
  bot.send_message(message, 'fuck you')
  
  bot.polling()
