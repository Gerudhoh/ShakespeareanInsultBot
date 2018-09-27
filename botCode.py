#!/usr/bin/python

import json
import requests

f = open("tok.txt", "r")

TOKEN = f.readline()

f.close()

URL = "https://api.telegram.org/bot{}/".format(TOKEN)

print ("token is: ", TOKEN)

