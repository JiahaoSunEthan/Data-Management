# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 23:09:09 2021

@author: 13451
"""
'''
import os
os.environ['JAVA_HOME']=r'C:\Program Files\Java\jdk1.8.0_291'
os.environ['SPARK_HOME'] = r"C:\sparkhadoop\spark-3.1.1-bin-hadoop3.2"
os.environ["PYSPARK_PYTHON"]=r"D:\Anaconda\python"
'''

from pyspark.sql import SparkSession
spark = SparkSession\
    .builder\
    .appName('readfile')\
    .getOrCreate()

country = spark.read.json('country.json')
ans = country.rdd.filter(lambda r: r['Continent'] == 'North America').map(lambda r:r['Name']).collect()
for item in ans:
    print(item)