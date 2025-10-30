
import telebot
import os

TOKEN = os.getenv("TOKEN")
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "👋 مرحبا زاكي! بوتك شغال بنجاح 🎯")

bot.infinity_polling()
