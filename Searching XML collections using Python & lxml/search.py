# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 14:23:05 2021

@author: 13451
"""

from lxml import etree
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument("xmlfile", help = 'index.xml')
parser.add_argument("folder", help = 'input file')
parser.add_argument("words", help = 'words to search')
args = vars(parser.parse_args())
#print(args)
#print(args["xmlfile"],args["folder"],args["words"])


f = open(args["xmlfile"])
tree = etree.parse(f)
    
check = set()  #using a set for deduplication of the print out content 
words = args["words"]
wl = words.split()
for word in wl:
    which_path = '/index/token[value =\'' + word+ '\']/provenance/which'
    which_ele = tree.xpath(which_path) # return the list of which elements
    where_path = '/index/token[value =\'' + word+ '\']/provenance/where'
    where_ele = tree.xpath(where_path) # return the list of where elements

    for i in range(len(which_ele)): # loop the two lists at the same time
        file_name = which_ele[i].text 
        f1 = open(args["folder"] +'\\' +file_name)
        tree1 = etree.parse(f1)
    
        ele_path_lst = where_ele[i].text.split('.')
        if '@' in ele_path_lst[-1]: # deal with the print_path with '@' or without '@'
            print_path = '/'+'/'.join(ele_path_lst[:-1])+ '['+ ele_path_lst[-1] + '=\'' + word +'\']'
        else:
            print_path = '/'+'/'.join(ele_path_lst)+'[contains(.,'+'\''+ word + '\')]'
            
            
        for item in tree1.xpath(print_path):
            # check if the same content has been printed before
            if (etree.tostring(item).decode('utf-8').strip(),file_name) in check:
                continue
            else:
                check.add((etree.tostring(item).decode('utf-8').strip(),file_name)) 
                print('Element:'+etree.tostring(item).decode('utf-8').strip())
                print('File:'+file_name)
            


        
#search('dfs replication')
