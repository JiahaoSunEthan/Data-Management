# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 18:40:14 2021

@author: 13451
"""

import sys
import mysql.connector
import json

args = sys.argv[:]

mydb = mysql.connector.connect(
  host="localhost",      
  user="dsci551",    
  passwd="Dsci-551",
  database = 'dsci551'
)
mycursor = mydb.cursor()

mycursor.execute('select name, participating_from from roster where name not in(select distinct name from chat)')
myresult = mycursor.fetchall()


ans_json = []
for item in myresult:
    ans_json.append({"Name": item[0], "Participating from": item[1]})

mydb.commit()
mycursor.close()
mydb.close()

#output
with open(args[1],'w') as f:
    json.dump(ans_json, f, indent = 4)
