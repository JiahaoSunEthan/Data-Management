# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 15:52:24 2021

@author: 13451
"""

#load csv file
import pandas as pd
data = pd.read_csv("D:\\USC\\DSCI551\\hw1\\551-tue-roster-updated.csv")

#format name
new_name = []
for name in data['Name']:
    new_name.append(name.split(',')[1].strip()+' '+name.split(',')[0].strip())
data.insert(1,'Name_re',new_name)
del data['Name']

#data collected from question 1a
f = open("D:\\USC\\DSCI551\\hw1\\551-0119-updated.txt",mode = "r",encoding = 'UTF-8')
dat = f.readlines()
f.close()

new_dt=[]
for item in dat:
    if item.isspace()==False:
        element = []
        element.append(item[0:8])
        element.append(item[9:].split(":")[0])
        element.append(item[9:].split(":")[1].strip())
        new_dt.append(element)

import pandas as pd
df = pd.DataFrame(new_dt,columns = ['Time','Person','Message']) 
ans = set()
for item in df['Person']:
    ans.add(item)

#search the dataframe and generate the result
result=[]
for i in range(len(data['Name_re'])):
    if data.loc[i,'Name_re']not in ans:
        result.append({"Name":data.loc[i,'Name_re'],"Participating from":data.loc[i,'Participating from']})

#convert into json
import json
json_file = open('output_file_1b.json','w')
ans_json = json.dumps(result)
json.dump(ans_json,json_file)

