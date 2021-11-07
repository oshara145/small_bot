import os
import telebot

bot = telebot.Telebot('api key here')

@bot.message_handler(commands=['start'])
def send_welcome(message):
  bot.reply_to(message,'Hello! Im' Uvindu Bro Chat Bot')

@bot.message_handler(commands=['how])
def send_message(message):
  bot.send_message(message, 'fuck you')
  
  bot.polling()