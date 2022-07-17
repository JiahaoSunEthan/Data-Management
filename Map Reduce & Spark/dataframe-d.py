# -*- coding: utf-8 -*-
"""
Created on Fri Apr 23 22:47:45 2021

@author: 13451
"""



from pyspark.sql import SparkSession

spark = SparkSession\
    .builder\
    .appName('readfile')\
    .getOrCreate()

countrylanguage = spark.read.json('countrylanguage.json') 
countrylanguage[countrylanguage.CountryCode == 'CAN'][['Language']].show()