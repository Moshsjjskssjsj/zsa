import telebot
import os

BOT_TOKEN = os.getenv("6647035961:AAGyIreqwuFhR85CLXUssVzuBoQuB7eSuS0")
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=["start"])
def start(msg):
    bot.reply_to(msg, "Bot is online!")

bot.polling()
