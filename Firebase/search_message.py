# -*- coding: utf-8 -*-
"""
Created on Fri Feb 12 23:20:58 2021

@author: 13451
"""

import requests
def search_message(name):
    reform_name = name.split(' ')[0].lower().capitalize()+ ' '+ name.split(' ')[1].lower().capitalize()
    url = r'https://dsci551-as1-default-rtdb.firebaseio.com/chats.json'+'?orderBy="Person"&equalTo="'+ reform_name +'"'
    response = requests.get(url)
    content = response.json()
    for key in content:
        print(content[key]['Time']+ '  '+ content[key]['Message'])
  
#test
search_message('jiayi lin')