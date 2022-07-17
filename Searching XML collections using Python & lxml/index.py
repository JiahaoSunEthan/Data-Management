# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 15:09:32 2021

@author: 13451
"""


def is_number(s): # check if the str consist of only arabic numbers
    try:
        float(s)
        return True
    except ValueError:
        pass
 
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
 
    return False

def tokenize(text): # tokenize the text and split it into a list
    import re
    reg = "[^0-9A-Za-z\u4e00-\u9fa5]"  # only preserve Chinese, arabic numbers, and lower and upper English letters
    l1 = text.split() #frist split with space
    result = []
    for item in l1:
        #print(re.sub(reg, ' ', text))
        str_tk = re.sub(reg, '', item)
        if is_number(str_tk) == True: # check if the str after token consists of only numbers
            if item[-1] == ',' or item[-1] =='.': #if the str end with ',' or '.', do not include the symbol
                result.append(item[:-1])
            else: 
                result.append(item)  # else return the original item, such as 49.95
        else:
            for element in re.sub(reg, ' ', item).split(): # replace all the symbols with space and split
                result.append(element)
    return result

def content_extract(file_name,result): # result is a dict, (key,value) pair is a (str, set) pair
    from lxml import etree, objectify
    file_path = 'input\\'+ file_name
    f = open(file_path)
    parser = etree.XMLParser(remove_comments= True)  #remove the commnets in the XML files
    tree = objectify.parse(f,parser=parser)

    root = tree.getroot()
    currentlevel = [[root,'']]  #the first element in the list of list saves the node, the second saves the path
    nextlevel = []
    while currentlevel: #level-order traverse for the tree
        for item in currentlevel:
            item[1] = item[1] + str(item[0].tag) +' ' #update the path
            if item[0].text is not None and len(item[0].text.strip())!=0: # check if the node contains text content, except spaces
                text_list = tokenize(item[0].text)  #tokenize the text
                for str_item in text_list:
                    if str_item in result.keys(): 
                        result[str_item].add(file_name+' '+ item[1].rstrip().replace(' ','.'))
                    else:
                        result[str_item] = set() # using set here for deduplication for the path
                        result[str_item].add(file_name+' '+ item[1].rstrip().replace(' ','.'))
            if len(item[0].attrib)!=0: # deal with the attributes
                for key in item[0].attrib.keys():
                    if item[0].attrib[key] in result.keys():
                        result[item[0].attrib[key]].add(file_name+' '+(item[1]+'@'+str(key)).replace(' ','.'))
                    else:
                        result[item[0].attrib[key]]= set()
                        result[item[0].attrib[key]].add(file_name+' '+(item[1]+'@'+str(key)).replace(' ','.'))
            for child_item in item[0]:
                nextlevel.append([child_item,item[1]])
        currentlevel = nextlevel
        nextlevel = []

import os

import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument("folder", help = 'input file')
parser.add_argument("xmlfile", help = 'index.xml')
args = vars(parser.parse_args())
 
file_dir = os.listdir(args["folder"])
result = dict()
for file_name in file_dir: # generate the result dict
    content_extract(file_name,result)

import xml.dom.minidom

doc = xml.dom.minidom.Document()
root = doc.createElement('index') #create root <index>
doc.appendChild(root)

for key in result:
    ndToken = doc.createElement('token')
    root.appendChild(ndToken)
    ndValue = doc.createElement('value')
    ndToken.appendChild(ndValue)
    ndValue.appendChild(doc.createTextNode(key))
    for item in result[key]:
        which = item.split()[0]
        where = item.split()[1]
        ndProvenance = doc.createElement('provenance')
        ndWhich = doc.createElement('which')
        ndWhich.appendChild(doc.createTextNode(which))
        ndWhere = doc.createElement('where')
        ndWhere.appendChild(doc.createTextNode(where))

        ndProvenance.appendChild(ndWhich)
        ndProvenance.appendChild(ndWhere)
        ndToken.appendChild(ndProvenance)


fw = open(args['xmlfile'], 'w')
doc.writexml(fw, addindent='\t', newl='\n', encoding="utf-8")
