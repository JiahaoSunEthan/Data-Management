# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 20:12:55 2021

@author: 13451
"""

import sys
import mysql.connector

args = sys.argv[:]

mydb = mysql.connector.connect(
  host="localhost",      
  user="dsci551",    
  passwd="Dsci-551",
  database = 'dsci551'
)
mycursor = mydb.cursor()


search_sql = """
    select time, contents
    from chat
    where lower(name) = %s
    """
mycursor.execute(search_sql, (args[1].lower(),))
#mycursor.execute(search_sql, ('zian fan',))
myresult = mycursor.fetchall()


if len(myresult)==0:
    print('This student is quiet or not founded.')
else:
    for item in myresult:
        print(item[0]+' '+ item[1])


mydb.commit()
mycursor.close()
mydb.close()

