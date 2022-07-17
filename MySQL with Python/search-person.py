# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 18:50:15 2021

@author: 13451
"""


import sys
import mysql.connector

args = sys.argv[:]
w = args[1].split(' ')


mydb = mysql.connector.connect(
  host="localhost",      
  user="dsci551",    
  passwd="Dsci-551",
  database = 'dsci551'
)
mycursor = mydb.cursor()

#create fulltext search 
#mycursor.execute('ALTER TABLE roster ADD FULLTEXT INDEX fulltext_name (name)')

#using regexp to match the exact word
if len(w) == 1:
    one_sql = """
    SELECT name FROM roster WHERE name REGEXP "\\\\b{}\\\\b"
    """.format(w[0])
    mycursor.execute(one_sql)
elif len(w) == 2:
    two_sql = """
    SELECT name FROM roster WHERE name REGEXP "\\\\b{}\\\\b"
    union 
    SELECT name FROM roster WHERE name REGEXP "\\\\b{}\\\\b"
    """.format(w[0],w[1])
    mycursor.execute(two_sql)

myresult = mycursor.fetchall()
for item in myresult:
    print(item[0])

mydb.commit()
mycursor.close()
mydb.close()

