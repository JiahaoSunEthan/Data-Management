# -*- coding: utf-8 -*-
"""
Created on Sat Mar 27 17:29:00 2021

@author: 13451
"""

import sys
args = sys.argv[:]

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",      
  user="dsci551",   
  passwd="Dsci-551",
  database = 'dsci551'
)
 
mycursor = mydb.cursor()
#mycursor.execute('create DATABASE dsci551')
#mycursor.execute('use dsci551')
mycursor.execute('DROP TABLE IF EXISTS chat ')
mycursor.execute('DROP TABLE IF EXISTS roster ')


create_roster_sql = """
CREATE TABLE roster(
    name varchar(70) PRIMARY KEY,
    participating_from varchar(50)
);
"""
mycursor.execute(create_roster_sql)

create_chat_sql = """
CREATE TABLE chat(
    id int PRIMARY KEY AUTO_INCREMENT,
    time varchar(10),
    name varchar(70),
    contents varchar(2000),
    FOREIGN KEY (name) REFERENCES roster (name)
);
"""
mycursor.execute(create_chat_sql)

#load roster csv file
import pandas as pd
data = pd.read_csv(args[2])

for index,row in data.iterrows():
    name = row['Name']
    new_name = name.split(',')[1].strip()+' '+name.split(',')[0].strip() # reform the name
    #print(new_name)
    #print(row['Participating from'])
    mycursor.execute('INSERT INTO roster(name, participating_from) VALUES (%s,%s)',(new_name,row["Participating from"]))

mycursor.execute('INSERT INTO roster(name,participating_from) values (%s,%s);',('Wensheng Wu', 'United States of America'))



#load chat log txt file
f = open(args[1],mode = "r",encoding = 'UTF-8')
chat_log = f.readlines()
f.close()

#remove empty str in the list & split each line
new_dt=[]
for item in chat_log:
    if item.isspace()==False:
        element = []
        element.append(item[0:8])
        element.append(item[9:].split(":")[0])
        element.append(item[9:].split(":")[1].strip())
        new_dt.append(element)

for item in new_dt:
    mycursor.execute('INSERT INTO chat(time, name, contents) values (%s,%s,%s)',(item[0], item[1], item[2]))
    

mydb.commit()
mycursor.close()
mydb.close()