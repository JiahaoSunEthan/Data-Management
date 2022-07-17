# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 18:24:32 2021

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

mycursor.execute('select name as Person, count(contents) as Message from chat group by name')
myresult = mycursor.fetchall()


ans_json = []
for item in myresult:
    ans_json.append({"Person": item[0], "Message": item[1]})

mydb.commit()
mycursor.close()
mydb.close()

#output
with open(args[1],'w') as f:
    json.dump(ans_json, f, indent = 4)
