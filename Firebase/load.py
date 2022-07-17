# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 16:47:28 2021

@author: 13451
"""


#load local json file
import json
f1 = open('output_file_2a.json')
chats = json.load(f1)
f2 = open('output_file_2b.json')
roster = json.load(f2)


#load data to firebase
import requests
url_roster = 'https://dsci551-as1-default-rtdb.firebaseio.com/roster.json'
response = requests.put(url_roster,roster)
url_chats = 'https://dsci551-as1-default-rtdb.firebaseio.com/chats.json'
response = requests.put(url_chats,chats)

