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
def insult_intel(bot, update):
    fTest = open("Shakespeare.txt", "r")
    x = random.randint(1, 23)
    for i in range(x):
      insult = fTest.readline()
 #   insult = fTest.readline()
    fTest.close()
    bot.sendMessage(chat_id=update.message.chat_id, text= insult)

intel_handler = CommandHandler('insult_intel', insult_intel);
dispatcher.add_handler(intel_handler)
#############################################################
def insult_char(bot, update):
    fp = open("Shakespeare.txt", "r")
    x = random.randint(21, 46)
    for i in range(x):
      insult = fp.readline()
    fp.close()
    bot.sendMessage(chat_id=update.message.chat_id, text= insult)

char_handler = CommandHandler('insult_char', insult_char);
dispatcher.add_handler(char_handler)
#############################################################
def insult_liars(bot, update):
    fp = open("Shakespeare.txt", "r")
    x = random.randint(48, 54)
    for i in range(x):
      insult = fp.readline()
    fp.close()
    bot.sendMessage(chat_id=update.message.chat_id, text= insult)

liar_handler = CommandHandler('insult_liars', insult_liars);
dispatcher.add_handler(liar_handler)


updater.start_polling()
updater.idle()

