#!/usr/bin/python3

import json
import requests
import telegram
import logging
import random

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
    fTest = open("Shakespeare.txt", "r")
    x = random.randint(1, 23)
    for i in range(x):
      insult = fTest.readline()
 #   insult = fTest.readline()
    fTest.close()
    bot.sendMessage(chat_id=update.message.chat_id, text= insult)

test_handler = CommandHandler('test_insult', test_insult);
dispatcher.add_handler(test_handler)
#############################################################
def intelligence(bot, update):
    fp = open("Shakespeare.txt", "r")
    x = 2
   # for i in range(x):
    insult = fp.readline()
    fTest.close()
    bot.sendMessage(chat_id=update.message.chat_id, text= insult)

intel_handler = CommandHandler('intelligence', intelligence);
dispatcher.add_handler(test_handler)

updater.start_polling()
#updater.idle()

