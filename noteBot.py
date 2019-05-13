#!/usr/bin/python3

#	chatbot.py
#	Developed by Julia Hohenadel

import json
import requests
import telegram
import logging

from telegram.error import NetworkError
from time import sleep
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

#Get the Token:
f = open("tok.txt", "r")
TOKEN = f.readline().strip()
f.close()

URL = "https://api.telegram.org/bot{}/".format(TOKEN)

bot = telegram.Bot(token = TOKEN)
bot = telegram.Bot(TOKEN, True, 4)
updater = Updater(TOKEN)
dispatcher = updater.dispatcher

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

#START##########################################################
def start(bot, update):
    bot.sendMessage(chat_id=update.message.chat_id, text="I'm a simple bot who really likes to take notes.")

start_handler = CommandHandler('start', start);
dispatcher.add_handler(start_handler)
#Show Notes##################################################
def add_note(note):
	#TO DO: Add functionality for this to update a text file
	fp = open("notes.txt", "a")
	fp.write(note)
	fp.write("\n")
	fp.close()
#Show Notes##################################################
def show_notes(bot, update):
	#TO DO: Add functionality for this to update a text file
	allNotes = "*Notes:*\n"
	
	with open('notes.txt') as fp:
		for line in fp:
			allNotes += line
			if len(line) == 1:
				break
	
	bot.sendMessage(chat_id=update.message.chat_id, text=allNotes, parse_mode="Markdown")

savings_handler = CommandHandler('show_notes', show_notes);
dispatcher.add_handler(savings_handler)
##################################################################  
def echo(bot, update):
	"""Echo the user message."""
	text = update.message.text.lower()
	
	what_is_noted = update.message.reply_to_message;
	
	if what_is_noted != None:
		newMsg = what_is_noted.text.lower()
		print(newMsg);
		add_note(newMsg)
		newMsg += " was noted"
		if text.find("noted") >= 0:
			bot.sendMessage(chat_id=update.message.chat_id, text=newMsg)
		
	if text.find("noted") >= 0 and what_is_noted == None:
		bot.sendMessage(chat_id=update.message.chat_id, text=text)	
	
dispatcher.add_handler(MessageHandler(Filters.text, echo))

updater.start_polling()
updater.idle()
