#!/usr/bin/python3

import json
import requests
import telegram
import logging

from telegram.ext import Updater, CommandHandler

#Get the Token:
f = open("tok.txt", "r")

TOKEN = f.readline().strip()
f.close()

#URL = "https://api.telegram.org/bot{}/".format(TOKEN)

bot = telegram.Bot(token = TOKEN)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

############################################################
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start);
dispatcher.add_handler(start_handler)
#############################################################
def test_insult(bot, update):
    fTest = open("test.txt", "r")
    insult = fTest.readline()
    bot.sendMessage(chat_id=update.message.chat_id, text= insult)

test_handler = CommandHandler('testInsult', testInsult);
dispatcher.add_handler(test_handler)

updater.start_polling()
#updater.idle()

