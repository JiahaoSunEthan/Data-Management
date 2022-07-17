# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 16:06:11 2021

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

#convert list into pandas dataframe
import pandas as pd
df = pd.DataFrame(new_dt,columns = ['Time','Person','Message']) 

#conunt and generate python dictionary
ans = dict()
for item in df['Person']:
    if item not in ans:
        ans[item] = 1
    else:
        ans[item]+= 1

#convert into json
ans_re = []
for key in ans:
    ans_re.append({"Person":key,"Message":ans[key]})

import json
json_file = open('output_file_1a.json','w')
ans_json = json.dumps(ans_re)
json.dump(ans_json,json_file)

#test
#f = open('output_file_1a.json')
#test = json.load(f)


