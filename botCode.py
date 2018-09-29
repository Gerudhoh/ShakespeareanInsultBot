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
def startIndex(startWord):
  fp = open("Shakespeare.txt", "r")
  counter = 1
  while 1:
    line=fp.readline()
    if line.strip() == startWord:
      fp.close()
      return counter + 1
    counter += 1
  fp.close()
############################################################
def endIndex(startIndex):
  fp = open("Shakespeare.txt", "r")
  counter = 1
  for i in range(startIndex):
     line=fp.readline()
     counter+=1
  while 1:
    line=fp.readline()
    if len(line.strip()) <= 10:
      fp.close()
      return counter
    counter+=1
  fp.close()
##################################################################
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")

start_handler = CommandHandler('start', start);
dispatcher.add_handler(start_handler)
    
##################################################################
def insult_intel(bot, update):
    start = startIndex("Smarts")
    send_text(bot, update, start, endIndex(start))

intel_handler = CommandHandler('insult_intel', insult_intel);
dispatcher.add_handler(intel_handler)
#############################################################
def insult_char(bot, update):
    start = startIndex("Character")
    send_text(bot, update, start, endIndex(start))
    
char_handler = CommandHandler('insult_char', insult_char);
dispatcher.add_handler(char_handler)
#############################################################
def insult_liars(bot, update):
    start = startIndex("Liars")
    send_text(bot, update, start, endIndex(start))
    
liar_handler = CommandHandler('insult_liars', insult_liars);
dispatcher.add_handler(liar_handler)
#############################################################
def insult_looks(bot, update):
    start = startIndex("Looks")
    send_text(bot, update, start, endIndex(start))
    
looks_handler = CommandHandler('insult_looks', insult_looks);
dispatcher.add_handler(looks_handler)
#############################################################
def insultingthreat(bot, update):
    start = startIndex("Threats")
    send_text(bot, update, start, endIndex(start))
    
threat_handler = CommandHandler('insultingthreat', insultingthreat);
dispatcher.add_handler(threat_handler)
#############################################################
def miscinsult(bot, update):
    start = startIndex("Other")
    send_text(bot, update, start, endIndex(start))
    
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

