#!/usr/bin/python3

import json
import requests
import telegram

f = open("tok.txt", "r")

TOKEN = f.readline().strip()
f.close()

#URL = "https://api.telegram.org/bot{}/".format(TOKEN)

bot = telegram.Bot(token = TOKEN)
print(bot.get_me())

