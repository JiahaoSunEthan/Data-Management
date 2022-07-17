# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 16:54:01 2021

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

#convert into json
ans_list=[]
for i in range(len(data['Name_re'])):
    ans_list.append({"Name":data.loc[i,'Name_re'],"Participating from":data.loc[i,'Participating from']})

import json
json_file = open('output_file_2b.json','w')
ans_json = json.dumps(ans_list)
json.dump(ans_json,json_file)