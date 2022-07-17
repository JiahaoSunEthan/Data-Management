# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 22:25:12 2021

@author: 13451
"""

import requests
def search_person(name):
    url = r'https://dsci551-as1-default-rtdb.firebaseio.com/roster.json'
    response = requests.get(url)
    content = response.json()
    for item in content:
        first_name = name.split(' ')[0].lower()
        last_name = name.split(' ')[1].lower()
        item_first_name = item['Name'].split(' ')[0].lower()
        item_last_name = item['Name'].split(' ')[1].lower()
        if first_name == item_first_name or first_name == item_last_name or last_name == item_first_name or last_name == item_last_name:
            print(item['Name'])

#test
#search_person('Max Chen')