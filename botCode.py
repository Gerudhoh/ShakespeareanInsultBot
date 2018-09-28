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
    
##################################################################
def insult_intel(bot, update):
    send_text(bot, update, 1, 23)

intel_handler = CommandHandler('insult_intel', insult_intel);
dispatcher.add_handler(intel_handler)
#############################################################
def insult_char(bot, update):
    send_text(bot, update, 21, 46)

char_handler = CommandHandler('insult_char', insult_char);
dispatcher.add_handler(char_handler)
#############################################################
def insult_liars(bot, update):
    send_text(bot, update, 48, 54)

liar_handler = CommandHandler('insult_liars', insult_liars);
dispatcher.add_handler(liar_handler)
#############################################################
def insult_looks(bot, update):
    send_text(bot, update, 56, 71)

looks_handler = CommandHandler('insult_looks', insult_looks);
dispatcher.add_handler(looks_handler)
#############################################################
def insultingthreat(bot, update):
    send_text(bot, update, 73, 77)

threat_handler = CommandHandler('insultingthreat', insultingthreat);
dispatcher.add_handler(threat_handler)
#############################################################
def miscinsult(bot, update):
    send_text(bot, update, 79, 93)

misc_handler = CommandHandler('miscinsult', miscinsult);
dispatcher.add_handler(misc_handler)
##################################################################
def send_text(bot, update, startIndex, endIndex):
    
    fp = open("Shakespeare.txt", "r")
    x = random.randint(startIndex, endIndex)
    for i in range(x):
      insult = fp.readline()
    fp.close()
    
    bot.sendMessage(chat_id=update.message.chat_id, text= insult)

updater.start_polling()
updater.idle()

