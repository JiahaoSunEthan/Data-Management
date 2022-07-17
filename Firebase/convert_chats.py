# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:47:33 2021

@author: 13451
"""

#load txt file
f = open("D:\\USC\\DSCI551\\hw1\\551-0119-updated.txt",mode = "r",encoding = 'UTF-8')
data = f.readlines()
f.close()

#remove empty str in the list & split each line
new_dt=[]
for item in data:
    if item.isspace()==False:
        element = []
        element.append(item[0:8])
        element.append(item[9:].split(":")[0])
        element.append(item[9:].split(":")[1].strip())
        new_dt.append(element)

#convert list into json
json_list = []
for i in range(len(new_dt)):
    json_list.append({'Time':new_dt[i][0],'Person':new_dt[i][1],'Message':new_dt[i][2]})

import json
json_file = open('output_file_2a.json','w')
ans_json = json.dumps(json_list)
json.dump(ans_json,json_file)